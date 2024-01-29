import numpy as np

# Create a 5x5 identity matrix and add 5 to it
identity_matrix = np.eye(5)
result_matrix = identity_matrix + 5
print("Resulting Matrix:\n", result_matrix)

# Create a 5x1 column vector with random integers between 1 and 10
column_vector = np.random.randint(1, 11, (5, 1))
print("Column Vector:", column_vector)

# Multiply the result_matrix with the column_vector
result_vector = np.dot(result_matrix, column_vector)

# Print the resulting vector
print("Resulting Vector:")
print(result_vector)
