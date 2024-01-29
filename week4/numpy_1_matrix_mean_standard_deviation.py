import numpy as np

# Create a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5, 5))

# Calculate the mean and standard deviation of the matrix
mean_value = np.mean(matrix)
std_deviation = np.std(matrix)

# Print the matrix, mean, and standard deviation
print("Random 5x5 Matrix:", matrix)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)
