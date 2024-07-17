import numpy as np

# Create matrices A and B with random integer values between 1 and 10
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

# Compute the sum of A and B
sum_matrix = np.add(A, B)

# Compute the difference between A and B
diff_matrix = np.subtract(A, B)

# Compute the element-wise product of A and B
element_wise_product = np.multiply(A, B)

# Compute the matrix product of A and B
matrix_product = np.dot(A, B)

# Compute the transpose of matrix A
transpose_A = np.transpose(A)

# Compute the determinant of matrix A
determinant_A = np.linalg.det(A)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nSum of A and B:")
print(sum_matrix)
print("\nDifference between A and B:")
print(diff_matrix)
print("\nElement-wise product of A and B:")
print(element_wise_product)
print("\nMatrix product of A and B:")
print(matrix_product)
print("\nTranspose of matrix A:")
print(transpose_A)
print("\nDeterminant of matrix A:")
print(determinant_A)
