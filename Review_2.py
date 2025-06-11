# review2_visuals.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings

warnings.filterwarnings('ignore')
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load datasets
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

# Preprocessing
deliveries.dropna(inplace=True)
matches['date'] = pd.to_datetime(matches['date'], errors='coerce')
matches['match_year'] = matches['date'].dt.year
combined_df = deliveries.merge(matches, left_on='match_id', right_on='id')

# 1. Win distribution by teams
wins = matches['winner'].value_counts()
fig = px.pie(
    values=wins.values,
    names=wins.index,
    title='Win Distribution by Teams',
    hole=0.3
)
fig.show()

# 2. Toss decision vs match winner
toss_vs_win = matches.groupby(['toss_decision', 'winner']).size().unstack().fillna(0)
toss_vs_win.T.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Toss Decision vs Match Winner')
plt.xlabel('Toss Decision')
plt.ylabel('Number of Wins')
plt.tight_layout()
plt.show()

# 3. Top 10 stadiums by number of matches
venue_counts = matches['venue'].value_counts().head(10)
sns.barplot(x=venue_counts.values, y=venue_counts.index, palette='Set2')
plt.title('Top 10 Stadiums by Number of Matches')
plt.xlabel('Match Count')
plt.ylabel('Venue')
plt.tight_layout()
plt.show()

# 4. Average runs scored per team per match
avg_runs = deliveries.groupby('batting_team')['total_runs'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=avg_runs.values, y=avg_runs.index, palette='Blues_r')
plt.title('Average Runs per Team per Match')
plt.xlabel('Average Runs')
plt.ylabel('Team')
plt.tight_layout()
plt.show()

# 5. Top 10 run scorers (interactive)
top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
fig = px.bar(
    x=top_scorers.values,
    y=top_scorers.index,
    orientation='h',
    labels={'x': 'Runs', 'y': 'Batsman'},
    title='Top 10 Run Scorers',
    color=top_scorers.values,
    color_continuous_scale='teal'
)
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()

# 6. Year-wise match trends
matches_per_year = matches.groupby('match_year').size()
sns.lineplot(x=matches_per_year.index, y=matches_per_year.values, marker='o', color='green')
plt.title('Year-wise IPL Match Count')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Heatmap of average runs per over by team
heatmap_data = deliveries.groupby(['batting_team', 'over'])['total_runs'].mean().unstack()
sns.heatmap(heatmap_data, cmap='coolwarm', linewidths=0.5, annot=True, fmt=".1f")
plt.title('Average Runs per Over by Batting Team')
plt.xlabel('Over')
plt.ylabel('Team')
plt.tight_layout()
plt.show()
