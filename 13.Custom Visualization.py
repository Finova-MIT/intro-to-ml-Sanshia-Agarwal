import numpy as np

import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 5))

# Plot with custom colors and labels
plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='green', linestyle='-', linewidth=2)

# Add title and labels
plt.title('Sine and Cosine Waves', fontsize=16, fontweight='bold')
plt.xlabel('X-axis (radians)', fontsize=12)
plt.ylabel('Y-axis (amplitude)', fontsize=12)

# Customize legend
plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True)

# Add grid
plt.grid(color='gray', linestyle=':', linewidth=0.5)

# Show the plot
plt.show()