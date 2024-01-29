import numpy as np

# Create a 5x5 matrix filled with random floats between 0 and 1.

arr = np.random.rand(5, 5)

# Replace the maximum value in the matrix with 0 and Print the original and modified matrices.

print("Unmodified matrix", arr)

max_index = np.unravel_index(np.argmax(arr), arr.shape)

arr[max_index] = 0

print("Modified matrix", arr)
