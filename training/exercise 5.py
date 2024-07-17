import numpy as np
import time
import numba

# Part (a) Vectorization

# Function to compute element-wise square using a for loop
def square_for_loop(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

# Function to compute element-wise square using NumPy vectorization
def square_vectorized(arr):
    return arr ** 2

# Create a large array of size 1,000,000
large_array = np.random.rand(1_000_000)

# Measure performance of the for loop function
start_time = time.time()
result_for_loop = square_for_loop(large_array)
end_time = time.time()
time_for_loop = end_time - start_time

# Measure performance of the vectorized function
start_time = time.time()
result_vectorized = square_vectorized(large_array)
end_time = time.time()
time_vectorized = end_time - start_time

print("Time taken using for loop:", time_for_loop, "seconds")
print("Time taken using vectorized operation:", time_vectorized, "seconds")

# Part (b) Numba

# Function to compute element-wise square using a for loop optimized with Numba
@numba.jit(nopython=True)
def square_for_loop_numba(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

# Measure performance of the Numba-optimized function
start_time = time.time()
result_for_loop_numba = square_for_loop_numba(large_array)
end_time = time.time()
time_for_loop_numba = end_time - start_time

print("Time taken using Numba-optimized for loop:", time_for_loop_numba, "seconds")
