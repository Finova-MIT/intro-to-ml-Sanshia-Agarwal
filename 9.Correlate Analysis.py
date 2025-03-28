import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Example data
np.random.seed(42)
data = pd.DataFrame(
    np.random.rand(10, 5),
    columns=['A', 'B', 'C', 'D', 'E']
)

# Compute the correlation matrix
correlation_matrix = data.corr()

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()