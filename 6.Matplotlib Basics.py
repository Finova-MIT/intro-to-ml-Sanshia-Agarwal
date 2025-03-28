import matplotlib.pyplot as plt

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Line Chart', color='blue', marker='o')
plt.title('Simple Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 7, 6, 8, 7]
plt.figure(figsize=(8, 4))
plt.scatter(x_scatter, y_scatter, label='Scatter Plot', color='red')
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()