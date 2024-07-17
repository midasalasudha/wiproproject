import numpy as np

# Part (a) Mathematical functions
values = np.linspace(0, 2 * np.pi, 10)
sine_values = np.sin(values)
cosine_values = np.cos(values)
tangent_values = np.tan(values)

print("Sine values:", sine_values)
print("Cosine values:", cosine_values)
print("Tangent values:", tangent_values)

# Part (b) Statistical functions
random_array = np.random.randint(1, 101, (3, 3))

mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_deviation = np.std(random_array)
variance_value = np.var(random_array)

print("\nRandom Array:\n", random_array)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
print("Variance:", variance_value)
