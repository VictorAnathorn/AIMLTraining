import numpy as np

# Create an 8x8 array filled with zeros
array = np.zeros((8, 8), dtype=int)

# Set the outer border elements to 1
array[0, :] = 1  # First row
array[-1, :] = 1  # Last row
array[:, 0] = 1  # First column
array[:, -1] = 1  # Last column

# Print the resulting array
print(array)
