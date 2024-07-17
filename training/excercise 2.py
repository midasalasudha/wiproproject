import numpy as np

# Part (a) Array arithmetic
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Part (b) Indexing and slicing
array_5x5 = np.arange(1, 26).reshape(5, 5)

subarray = array_5x5[:2, :2]

print("\nSubarray (first two rows and columns):")
print(subarray)

# Part (c) Boolean indexing
array_10_to_19 = np.arange(10, 20)

extracted_elements = array_10_to_19[array_10_to_19 > 15]

print("\nElements greater than 15:", extracted_elements)
