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

