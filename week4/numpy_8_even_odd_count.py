
import numpy as np

# Create a 1D array of 20 random integers between 1 and 100
random_array = np.random.randint(1, 101, 20)
print(random_array % 2 == 0)
print(random_array % 2 != 0)


# Calculate the number of even and odd elements
even_count = np.sum(random_array % 2 == 0)
odd_count = np.sum(random_array % 2 != 0)

# Print the original array and the counts of even and odd elements
print("Random 1D Array:")
print(random_array)

print("\nNumber of even elements:", even_count)
print("Number of odd elements:", odd_count)
