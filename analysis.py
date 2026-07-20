import kagglehub    
import pandas as pd

#Fetching Kaggle Lichess game data
print('Loading games.csv...')
download_dir = kagglehub.dataset_download("datasnaek/chess")
#Combine foldder path with file name
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
