
# Import the NumPy library and alias it as np
import numpy as np

# Create a 1D NumPy array containing values from 1 to 9 using np.arange(1, 10)
# and then reshape it into a 3x3 matrix using .reshape(3, 3)
arr = np.arange(1, 10).reshape(3, 3)

# Calculate the trace of the 3x3 matrix using np.trace()
result = np.trace(arr)

# Print the result
print(result)
