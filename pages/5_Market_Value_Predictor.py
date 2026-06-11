import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

st.title("💰 Market Value Predictor")

BASE_DIR = Path(__file__).resolve().parent.parent

# Load model
model = pickle.load(
    open(
        BASE_DIR / "models" / "market_value_model.pkl",
        "rb"
    )
)

st.markdown("""
Predict a football player's estimated market value based on performance statistics.
""")

# User Inputs
age = st.slider(
    "Age",
    min_value=16,
    max_value=45,
    value=25
)

matches = st.number_input(
    "Matches Played",
    min_value=0,
    value=50
)

minutes_played = st.number_input(
    "Minutes Played",
    min_value=0,
    value=3000
)

goals = st.number_input(
    "Goals",
    min_value=0,
    value=10
)

assists = st.number_input(
    "Assists",
    min_value=0,
    value=5
)

international_caps = st.number_input(
    "International Caps",
    min_value=0,
    value=10
)

international_goals = st.number_input(
    "International Goals",
    min_value=0,
    value=2
)

# Predict Button
if st.button("Predict Market Value"):

    input_data = pd.DataFrame(
        {
            "age": [age],
            "matches": [matches],
            "minutes_played": [minutes_played],
            "goals": [goals],
            "assists": [assists],
            "international_caps": [international_caps],
            "international_goals": [international_goals]
        }
    )

    prediction_log = model.predict(input_data)[0]

    # Convert back from log scale
    prediction = np.expm1(prediction_log)

    st.success(
        f"Estimated Market Value: €{prediction:,.0f}"
    )