import pandas as pd

# Load the matches CSV file into a DataFrame
matches_df = pd.read_csv('matches.csv')

# Display the first few rows of the DataFrame
print(matches_df.head())

# Filter the DataFrame for matches played in 2019
matches_2019 = matches_df[matches_df['season'] == 2019]
print("Matches played in 2019:")
print(matches_2019)

# Count the number of wins for each team
team_wins = matches_df['winner'].value_counts()

# Convert the Series to a DataFrame for sorting
team_wins_df = team_wins.reset_index()
team_wins_df.columns = ['team', 'wins']

# Sort the DataFrame by 'wins' in descending order
sorted_matches = team_wins_df.sort_values(by='wins', ascending=False)
print("Teams sorted by number of wins:")
print(sorted_matches.head())

# Set the 'id' column as the index
matches_df.set_index('id', inplace=True)
print("DataFrame with 'id' as the index:")
print(matches_df.head())