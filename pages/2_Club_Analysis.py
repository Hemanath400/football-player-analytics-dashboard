import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("🏟 Club Analysis")

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "clustered_players.csv"
)

st.subheader("Top Clubs by Squad Value")

club_value = (
    df.groupby("current_club_name")
    ["market_value_in_eur"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

fig = px.bar(
    club_value,
    x="market_value_in_eur",
    y="current_club_name",
    orientation="h",
    title="Top 20 Clubs by Squad Value"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Oldest Squads")

club_age = (
    df.groupby("current_club_name")
    ["age"]
    .mean()
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

fig2 = px.bar(
    club_age,
    x="age",
    y="current_club_name",
    orientation="h",
    title="Average Age by Club"
)

st.plotly_chart(fig2, use_container_width=True)