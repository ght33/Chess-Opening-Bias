import kagglehub    
import pandas as pd

#Fetching Kaggle Lichess game data
print('Loading games.csv...')
download_dir = kagglehub.dataset_download("datasnaek/chess")
#Combine folder path with file name
csv_path = f"{download_dir}/games.csv"

print(f'Loading data from cloud cache: {csv_path}')
df = pd.read_csv(csv_path)

print(f"Loaded {len(df)} games.")

#Defining needed columns
cols = ['white_rating', 'black_rating', 'winner', 'opening_name']

print('\nVerifying columns:')
for c in cols:
    print(f"  {c}: {c in df.columns}")

#Checking for missing data
print("\nMissing values:")
print(df[cols].isnull().sum())

# Baseline Win Rate
print("\n---Baseline Win Rates ---")

# Count raw total outcomes of winner column
print("Value counts for winner")
print(df['winner'].value_counts())

#Calculate % breakdown of total wins
print("\nPercentage breakdown:")
print(df['winner'].value_counts(normalize=True) * 100)


#Naive Win Rate 

print('\n--- Naive Win Rates By Opening ---')

#Filter rare openings
opening_counts = df['opening_name'].value_counts()
common_openings = opening_counts[opening_counts >= 50].index

#Calculating White win rate per opening
naive = df[df['opening_name'].isin(common_openings)].groupby('opening_name').apply(
    lambda g: (g['winner'] == 'white').mean()
).sort_values(ascending=False)

# Display t10 openings
print("Top 10 openings by White win rate:")
print(naive.head(10))


#Rating Adjusted Preformance

#Calculating rating diff of each game
df['rating_diff'] = df['white_rating'] - df['black_rating']

#Calculating expected outcome using ELO formula
df['expected_white_win'] = 1 / (1 + 10 ** (-df['rating_diff'] / 400))

#Calculating actual win
df['white_won'] = (df['winner'] == 'white').astype(int)

#Preformance over expectation (POE0) per game 
df['poe'] = df['white_won'] - df['expected_white_win']

#Aggregate by opening to find true opening advantage
adjusted = (
    df[df['opening_name'].isin(common_openings)]
    .groupby('opening_name')['poe']
    .agg(['mean', 'count'])
    .sort_values(by='mean', ascending=False)
    )
print('\nTope 10 Openings by Preformance Over Expectation POE:')
print(adjusted.head(10))
