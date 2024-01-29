import numpy as np

# Create a 10x10 matrix filled with random integers between 1 and 100.

arr = np.random.randint(1, 101, (10, 10))

# Find the minimum and maximum values of the matrix along with their indices.

max_index = np.unravel_index(np.argmax(arr), arr.shape)
min_index = np.unravel_index(np.argmin(arr), arr.shape)


print(f"The max value is at the index {max_index} and the value is {arr[max_index]}")
print(f"The min value is at the index {min_index} and the value is {arr[min_index]}")
