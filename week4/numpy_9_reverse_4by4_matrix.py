import numpy as np

A = np.arange(1, 17).reshape(4, 4)

print("Original matrix:\n", A)
print("Reversed matrix:\n", A[:, ::-1])
print("Reversed matrix:\n", A[::-1, ::-1])
