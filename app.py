import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Football Analytics Dashboard",
    page_icon="⚽",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "clustered_players.csv"
)

# Title
st.title("⚽ Football Player Analytics Dashboard")

st.markdown("""
### Project Overview

This dashboard analyzes football players using:

- Performance Analytics
- KMeans Clustering
- PCA Visualization
- Similar Player Recommendation System

**Tech Stack**

Python • Pandas • Scikit-Learn • Plotly • Streamlit
""")

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Players", f"{len(df):,}")
col2.metric("Clubs", df["current_club_name"].nunique())
col3.metric("Avg Age", round(df["age"].mean(), 1))
col4.metric(
    "Avg Market Value (€)",
    f"{int(df['market_value_in_eur'].mean()):,}"
)

# Market Value Distribution
st.subheader("💰 Market Value Distribution")

fig = px.histogram(
    df,
    x="market_value_in_eur",
    nbins=50
)

st.plotly_chart(fig, use_container_width=True)

# Top Players
st.subheader("⭐ Top 10 Most Valuable Players")

top_players = (
    df.nlargest(
        10,
        "market_value_in_eur"
    )[
        [
            "name",
            "current_club_name",
            "market_value_in_eur"
        ]
    ]
)

st.dataframe(
    top_players,
    use_container_width=True
)