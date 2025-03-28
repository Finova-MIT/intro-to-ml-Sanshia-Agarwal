import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Perform basic operations
array_sum = array_1d + 10
print("Array after addition:", array_sum)

array_product = array_1d * 2
print("Array after multiplication:", array_product)

# Access elements
element = array_2d[1, 2]  # Access element at row 1, column 2
print("Accessed Element:", element)

# Slicing
sliced_array = array_1d[1:4]  # Slice from index 1 to 3
print("Sliced Array:", sliced_array)

# Reshape array
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# Create arrays with zeros
zeros_array = np.zeros((2, 3))
print("Zeros Array:\n", zeros_array)

# Create arrays with ones
ones_array = np.ones((3, 2))
print("Ones Array:\n", ones_array)

# Create arrays with random values
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)

# Perform basic arithmetic operations
array_diff = array_1d - 2
print("Array after subtraction:", array_diff)

array_div = array_1d / 2
print("Array after division:", array_div)

# Mean
array_mean = np.mean(array_1d)
print("Mean of array:", array_mean)

# Median
array_median = np.median(array_1d)
print("Median of array:", array_median)

# Sum
array_sum_total = np.sum(array_1d)
print("Sum of array:", array_sum_total)

