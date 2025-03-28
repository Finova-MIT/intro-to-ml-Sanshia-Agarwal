import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('matches.csv')

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

# Handle missing values
# Drop rows with missing values (or use df.fillna() for imputation)
df_cleaned = df.dropna()

# Display basic statistics
print("\nBasic Statistics:")
print(df_cleaned.describe())

# Perform analysis (example: correlation matrix)
correlation_matrix = df_cleaned.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualize key insights
# Example 1: Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Example 2: Distribution of a specific column (replace 'column_name' with an actual column)
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned['column_name'], kde=True, bins=30)
plt.title('Distribution of Column: column_name')
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()

# Example 3: Scatter plot between two columns (replace 'col_x' and 'col_y' with actual columns)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x='col_x', y='col_y')
plt.title('Scatter Plot: col_x vs col_y')
plt.xlabel('col_x')
plt.ylabel('col_y')
plt.show()