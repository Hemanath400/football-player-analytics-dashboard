# ⚽ Football Player Analytics Dashboard

## 📌 Project Overview

Football Player Analytics Dashboard is an end-to-end Data Science project built using Transfermarkt football data.

The dashboard provides insights into player performance, club statistics, player clustering, and player recommendations using Machine Learning techniques.

The project demonstrates:

- Data Cleaning
- Feature Engineering
- K-Means Clustering
- PCA Visualization
- Recommendation System
- Streamlit Deployment

---

## 🚀 Live Demo

**Streamlit App:**

**[Football Analytics Dashboard · Streamlit](https://football-player-analytics-dashboard-hmhbw7xarc73yf2gjymstq.streamlit.app/)**

**GitHub Repository:**

[Hemanath400/football-player-analytics-dashboard](https://github.com/Hemanath400/football-player-analytics-dashboard)

🎯 Project Objectives

- Analyze football player performance
- Explore club-level statistics
- Group similar players using K-Means Clustering
- Visualize player styles using PCA
- Recommend similar players based on performance metrics
- Build an interactive dashboard for football analytics

---

## 📊 Dataset

**Source:** Transfermarkt Football Dataset

### Dataset Size

- Players: 17,467+
- Clubs: 768+
- Appearances: 1.8 Million+

---

## 🛠️ Tech Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Plotly
- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- K-Means Clustering
- PCA
- Nearest Neighbors Recommendation System

### Deployment

- Streamlit
- GitHub

---

## 🔍 Features

### ⚽ Player Explorer

- Search players
- View player statistics
- Analyze performance metrics

### 🏟️ Club Analysis

- Club-wise player distribution
- Average market value
- Club performance insights

### 🧩 Player Clustering

Players are grouped using K-Means Clustering based on:

- Goals
- Assists
- Minutes Played
- International Statistics

### 📈 PCA Visualization

- Dimensionality reduction
- Interactive cluster visualization
- Player style exploration

### 🤝 Similar Player Recommendation

Recommend players based on:

- Goals
- Assists
- Minutes Played
- International Experience

Uses Nearest Neighbors similarity search.

---

## 📈 Machine Learning Workflow

### Data Cleaning

- Removed duplicates
- Handled missing values
- Corrected data types

### Feature Engineering

Created features such as:

- Age
- Total Contributions
- Goal Contribution Rate
- Experience Metrics

### Scaling

Used StandardScaler for feature normalization.

### Clustering

Applied K-Means Clustering to identify player groups.

### PCA

Reduced feature dimensions for visualization.

### Recommendation Engine

Built a similarity-based recommendation system using Nearest Neighbors.

---

## 📂 Project Structure

```text
football-player-analytics-dashboard/

├── app.py
├── data/
│   └── processed/
│       └── clustered_players.csv

├── models/
│   ├── kmeans_model.pkl
│   ├── pca.pkl
│   └── scaler.pkl

├── pages/
│   ├── 1_Player_Explorer.py
│   ├── 2_Club_Analysis.py
│   ├── 3_Player_Clusters.py
│   └── 4_Similar_Players.py

├── notebooks/
├── requirements.txt
└── README.md
```
