import numpy as np
import time

# Part (a) Broadcasting
array_3x1 = np.array([[1], [2], [3]])
array_1x3 = np.array([4, 5, 6])

result_broadcasting = array_3x1 + array_1x3

print("Result of Broadcasting:\n", result_broadcasting)

# Part (b) Vectorized operations
large_array1 = np.random.rand(1_000_000)
large_array2 = np.random.rand(1_000_000)

start_time = time.time()
elementwise_product = large_array1 * large_array2
end_time = time.time()

computation_time = end_time - start_time

print("\nTime taken for element-wise product using vectorized operations:", computation_time, "seconds")
