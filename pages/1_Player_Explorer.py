import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

import streamlit as st

st.title("TEST PAGE")

st.success("Player Explorer is working")

st.title("👤 Player Explorer")

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "clustered_players.csv"
)

player = st.selectbox(
    "Select Player",
    sorted(df["name"].dropna().unique())
)

player_data = df[df["name"] == player]

st.subheader("Player Details")

cols = [
    "name",
    "position_group",
    "age",
    "goals",
    "assists",
    "market_value_in_eur",
    "cluster_name"
]

st.dataframe(player_data[cols])

fig = px.bar(
    x=["Goals", "Assists"],
    y=[
        player_data["goals"].iloc[0],
        player_data["assists"].iloc[0]
    ],
    title=f"{player} Performance"
)

st.plotly_chart(fig, use_container_width=True)