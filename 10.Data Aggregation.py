import pandas as pd

import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'C', 'A'],
    'Values': [10, 20, 15, 25, 30, 10, 35, 20, 40, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by 'Category' and calculate the sum of 'Values'
grouped_data = df.groupby('Category')['Values'].sum()

# Visualize the results
grouped_data.plot(kind='bar', color=['blue', 'green', 'orange'], figsize=(8, 5))
plt.title('Sum of Values by Category')
plt.xlabel('Category')
plt.ylabel('Sum of Values')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()