import numpy as np

import matplotlib.pyplot as plt

# Data for the plots
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]
scatter_x = np.random.rand(50)
scatter_y = np.random.rand(50)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axs[0, 0].plot(x, y, label='sin(x)', color='blue')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Bar plot
axs[0, 1].bar(categories, values, color='orange')
axs[0, 1].set_title('Bar Plot')

# Scatter plot
axs[1, 0].scatter(scatter_x, scatter_y, color='green', alpha=0.7)
axs[1, 0].set_title('Scatter Plot')

# Empty subplot (optional for layout)
axs[1, 1].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()