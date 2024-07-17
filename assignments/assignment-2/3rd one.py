import numpy as np
from scipy.misc import derivative

def f(x):
    return x*3 + 2*x*2 + x + 1
[10:55 AM, 6/5/2024] bhargavi: # First derivative
f_prime = derivative(f, 1, dx=1e-6)
print("First derivative of f(x) at x=1:", f_prime)

# Second derivative
f_double_prime = derivative(f, 1, n=2, dx=1e-6)
print("Second derivative of f(x) at x=1:", f_double_prime)
[10:55 AM, 6/5/2024] bhargavi: from scipy.integrate import quad

# Definite integral of f(x) from x=0 to x=2
integral, _ = quad(f, 0, 2)
print("Definite integral of f(x) from x=0 to x=2:", integral)