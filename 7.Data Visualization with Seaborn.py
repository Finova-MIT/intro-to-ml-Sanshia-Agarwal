import seaborn as sns 
import numpy as np

import matplotlib.pyplot as plt

# Generate sample data
data = np.random.normal(loc=50, scale=10, size=1000)

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Box plot
sns.boxplot(data, ax=axes[0], color='skyblue')
axes[0].set_title('Box Plot')

# Histogram
sns.histplot(data, bins=30, kde=False, ax=axes[1], color='lightgreen')
axes[1].set_title('Histogram')

# Density plot
sns.kdeplot(data, ax=axes[2], color='orange')
axes[2].set_title('Density Plot')

# Show the plots
plt.tight_layout()
plt.show()