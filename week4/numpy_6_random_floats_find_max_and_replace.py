import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

B = A[1:3, 0:2]


B[0, 0] = 100

print(B)
print(A)
