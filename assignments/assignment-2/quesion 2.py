
import numpy as np
from scipy.linalg import solve

# Coefficient matrix A
A = np.array([[2, 3], [3, 4]])

# Constant matrix B
B = np.array([8, 11])

# Solve the system of equations
X = solve(A, B)

# Extracting the values of x and y
x = X[0]
y = X[1]

print("The solution for x is:", x)
print("The solution for y is:", y)