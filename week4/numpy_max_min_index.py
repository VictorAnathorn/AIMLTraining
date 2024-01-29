import numpy as np

# Create a 2D NumPy array
arr = np.array([[4, 2, 7],
                [1, 9, 5]])

# Find the index of the min and max value
min_index = np.unravel_index(np.argmin(arr), arr.shape)
max_index = np.unravel_index(np.argmax(arr), arr.shape)

print("Minimum value index:", min_index)
print("Maximum value index:", max_index)
