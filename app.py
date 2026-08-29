import streamlit as st
import pandas as pd
import kagglehub

st.set_page_config(page_title="Chess Opening Bias", layout="wide")

st.title("♟️ Chess Opening Bias & POE Explorer")
st.write("Isolating true opening utility by adjusting for rating differences using Performance Over Expectation (POE).")

# Load Data
@st.cache_data
def load_data():
    download_dir = kagglehub.dataset_download("datasnaek/chess")
    df = pd.read_csv(f"{download_dir}/games.csv")
    df['rating_diff'] = df['white_rating'] - df['black_rating']
    df['expected_white_win'] = 1 / (1 + 10 ** (-df['rating_diff'] / 400))
    df['white_won'] = (df['winner'] == 'white').astype(int)
    df['poe'] = df['white_won'] - df['expected_white_win']
    return df

df = load_data()

# Sidebar Filter
st.sidebar.header("Filter Settings")
min_games = st.sidebar.slider("Minimum Games Played", min_value=10, max_value=360, value=50, step=10)

# Aggregations
opening_stats = df.groupby('opening_name').agg(
    total_games=('winner', 'count'),
    raw_win_rate=('white_won', 'mean'),
    avg_poe=('poe', 'mean')
).reset_index()

filtered_stats = opening_stats[opening_stats['total_games'] >= min_games].sort_values(by='avg_poe', ascending=False)

# Display Visuals
st.subheader(f"Top Openings by Performance Over Expectation (Min {min_games} Games)")
st.dataframe(filtered_stats.head(10), use_container_width=True)

st.bar_chart(filtered_stats.head(10).set_index('opening_name')['avg_poe'])