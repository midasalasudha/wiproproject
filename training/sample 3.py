


# Define the function
def f(x):
    print('sin ', np.sin(x))
    return np.sin(x)


# Compute the first, second, and third derivatives at a point, say x=1
x_val = 1
f_prime = derivative(f, x_val, dx=1, n=1, order=3)
f_double_prime = derivative(f, x_val, dx=1, n=2, order=3)
f_triple_prime = derivative(f, x_val, dx=1, n=3, order=5)
print("Function: f(x) = sin(x)")
print(f"First Derivative at x = {x_val}: f'(x) =", f_prime)
print(f"Second Derivative at x = {x_val}: f''(x) =", f_double_prime)
print(f"Third Derivative at x = {x_val}: f'''(x) =", f_triple_prime)
