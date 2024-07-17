import numpy as np

# a. Create a 1-dimensional array
array_1d = np.arange(10)
print("1-D Array:")
print(array_1d)
print("Shape:", array_1d.shape)

# b. Create a 2-dimensional array
array_2d = np.arange(1, 10).reshape(3, 3)
print("\n2-D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Sum of all elements:", np.sum(array_2d))

# c. Reshape the array
reshaped_array = array_1d.reshape(2, 5)
print("\nReshaped Array:")
print(reshaped_array)
print("Shape:", reshaped_array.shape)
