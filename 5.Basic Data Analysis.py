import pandas as pd
import numpy as np

# Load the dataset
matches = pd.read_csv('matches.csv')

# Calculate descriptive statistics
mean_values = matches.mean(numeric_only=True)
median_values = matches.median(numeric_only=True)
std_dev_values = matches.std(numeric_only=True)

# Display the results
print("Mean Values:\n", mean_values)
print("\nMedian Values:\n", median_values)
print("\nStandard Deviation Values:\n", std_dev_values)