# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Set plot styles
sns.set(style='darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load datasets
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# Display initial data overview
print("Matches Dataset:")
print(matches.head())
print("\nDeliveries Dataset:")
print(deliveries.head())

# -------------------------------
# 1. Data Cleaning and Handling Missing Values
# -------------------------------

# Check for missing values in both datasets
print("\nMissing values in matches dataset:")
print(matches.isnull().sum())
print("\nMissing values in deliveries dataset:")
print(deliveries.isnull().sum())

# Fill missing values in 'player_of_match' with 'Unknown' to avoid losing records
matches['player_of_match'].fillna('Unknown', inplace=True)

# Drop rows with any missing values in 'deliveries' dataset to ensure complete data for analysis
deliveries.dropna(inplace=True)

# -------------------------------
# 2. Feature Selection and Engineering
# -------------------------------

# Convert 'date' column to datetime for time-based analysis
matches['date'] = pd.to_datetime(matches['date'], dayfirst=True, errors='coerce')

# Create 'match_year' feature for grouping matches by year
matches['match_year'] = matches['date'].dt.year

# Merge deliveries with match details for combined analysis
combined_df = deliveries.merge(matches, left_on='match_id', right_on='id')

# Calculate total runs scored in each match
total_runs_per_match = combined_df.groupby('match_id')['total_runs'].sum().reset_index()
total_runs_per_match.rename(columns={'total_runs': 'total_runs_in_match'}, inplace=True)

# Merge total runs per match back into the matches dataframe
matches = matches.merge(total_runs_per_match, left_on='id', right_on='match_id')

# -------------------------------
# 3. Ensuring Data Integrity and Consistency
# -------------------------------

# Standardize team names for consistency across datasets
team_replacements = {
    'Delhi Daredevils': 'Delhi Capitals',
    'Kings XI Punjab': 'Punjab Kings'
}
matches.replace({'team1': team_replacements, 'team2': team_replacements, 'winner': team_replacements}, inplace=True)
deliveries.replace({'batting_team': team_replacements, 'bowling_team': team_replacements}, inplace=True)

# -------------------------------
# 4. Summary Statistics and Insights
# -------------------------------

# Total matches played
total_matches = matches.shape[0]
print(f"\nTotal matches played: {total_matches}")

# Total runs scored
total_runs = deliveries['total_runs'].sum()
print(f"Total runs scored: {total_runs}")

# Top 5 run scorers
top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 run scorers:")
print(top_scorers)

# Top 5 wicket takers
wickets = deliveries[deliveries['dismissal_kind'].notnull()]
top_wicket_takers = wickets['bowler'].value_counts().head(5)
print("\nTop 5 wicket takers:")
print(top_wicket_takers)

# -------------------------------
# 5. Identifying Patterns, Trends, and Anomalies
# -------------------------------

# Runs per over - calculate average runs scored per over across all matches
runs_per_over = deliveries.groupby('over')['total_runs'].mean()
print("\nAverage runs per over:")
print(runs_per_over)

# Team-wise total runs
team_runs = deliveries.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
print("\nTotal runs by each team:")
print(team_runs)

# -------------------------------
# 6. Handling Outliers and Data Transformations
# -------------------------------

# Identify outliers in 'total_runs' using Interquartile Range (IQR) method
Q1 = deliveries['total_runs'].quantile(0.25)
Q3 = deliveries['total_runs'].quantile(0.75)
IQR = Q3 - Q1

# Filter deliveries considered outliers based on total runs
outliers = deliveries[(deliveries['total_runs'] < Q1 - 1.5 * IQR) | (deliveries['total_runs'] > Q3 + 1.5 * IQR)]
print(f"\nNumber of outlier deliveries: {outliers.shape[0]}")

# -------------------------------
# 7. Initial Visual Representation of Key Findings
# -------------------------------

# Top 5 run scorers bar plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_scorers.values, y=top_scorers.index, palette='viridis')
plt.title('Top 5 Run Scorers')
plt.xlabel('Runs')
plt.ylabel('Batsman')
plt.show()

# Runs per over line plot
plt.figure(figsize=(10,6))
sns.lineplot(x=runs_per_over.index, y=runs_per_over.values, marker='o')
plt.title('Average Runs per Over')
plt.xlabel('Over')
plt.ylabel('Average Runs')
plt.show()

# Top 5 wicket takers bar plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_wicket_takers.values, y=top_wicket_takers.index, palette='magma')
plt.title('Top 5 Wicket Takers')
plt.xlabel('Wickets')
plt.ylabel('Bowler')
plt.show()

# Team-wise total runs bar plot
plt.figure(figsize=(12,6))
sns.barplot(x=team_runs.values, y=team_runs.index, palette='coolwarm')
plt.title('Total Runs by Each Team')
plt.xlabel('Total Runs')
plt.ylabel('Team')
plt.show()
