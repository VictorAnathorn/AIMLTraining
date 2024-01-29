import numpy as np

# Create a 1000-element array of random integers between 1 and 1000
random_array = np.random.randint(1, 1001, 1000)

# Calculate the cumulative sum of the array
cumulative_sum = np.cumsum(random_array)

# Print the 10th, 100th, and 500th elements of the cumulative sum array
print("10th Element of Cumulative Sum:", cumulative_sum[9])   # 0-based index
print("100th Element of Cumulative Sum:", cumulative_sum[99])  # 0-based index
print("500th Element of Cumulative Sum:", cumulative_sum[499])  # 0-based index
