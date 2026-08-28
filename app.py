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

