import numpy as np

# Create two 3x3 matrices filled with random integers between 1 and 100.

matrix1 = np.random.randint(1, 101, (3, 3))

matrix2 = np.random.randint(1, 101, (3, 3))

# Compute their element-wise multiplication, and print the resulting matrix.

print(matrix1*matrix2)
