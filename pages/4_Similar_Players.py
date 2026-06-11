import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

st.title("🎯 Similar Player Finder")

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "clustered_players.csv"
)

features = [
    "goals_per90",
    "assists_per90",
    "cards_per90",
    "age",
    "log_market_value"
]

X = df[features].fillna(0)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

nn = NearestNeighbors(
    n_neighbors=6,
    metric="euclidean"
)

nn.fit(X_scaled)

player = st.selectbox(
    "Select Player",
    sorted(df["name"].dropna().unique())
)

idx = df[df["name"] == player].index[0]

distances, indices = nn.kneighbors(
    [X_scaled[idx]]
)

recommendations = df.iloc[
    indices[0]
][
    [
        "name",
        "position_group",
        "age",
        "market_value_in_eur",
        "cluster_name"
    ]
]

st.subheader("Most Similar Players")

st.dataframe(recommendations)