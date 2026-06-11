import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("⚽ Player Style Clusters")

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "clustered_players.csv"
)

st.subheader("PCA Cluster Visualization")

fig = px.scatter(
    df,
    x="PC1",
    y="PC2",
    color="cluster_name",
    hover_name="name",
    title="Player Clusters"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Cluster Distribution")

cluster_counts = (
    df["cluster_name"]
    .value_counts()
    .reset_index()
)

cluster_counts.columns = [
    "cluster",
    "count"
]

fig2 = px.pie(
    cluster_counts,
    names="cluster",
    values="count"
)

st.plotly_chart(fig2, use_container_width=True)

selected_cluster = st.selectbox(
    "Select Cluster",
    sorted(df["cluster_name"].unique())
)

st.dataframe(
    df[df["cluster_name"] == selected_cluster][
        [
            "name",
            "position_group",
            "age",
            "market_value_in_eur"
        ]
    ]
)