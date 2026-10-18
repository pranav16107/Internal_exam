# Q1 (Short, Week 10). Write a Python program using SymPy to check whether (3x² + 4xy) dx + (2x² + 2y) dy = 0 is exact and, if so, print its general solution.

import sympy as sp
from sympy import symbols, diff, integrate, simplify

# Define variables
x, y = symbols('x y')

# Define M and N
M = 3*x**2 + 4*x*y
N = 2*x**2 + 2*y

print("Given differential equation: M dx + N dy = 0")
print("M =", M)
print("N =", N)

# Calculate partial derivatives
dM_dy = diff(M, y)
dN_dx = diff(N, x)

print("dM/dy =", dM_dy)
print("dN/dx =", dN_dx)

# Check exactness
check = simplify(dM_dy - dN_dx)
print("Exactness check =", check)

if check == 0:
    # Find potential function
    psi_x = integrate(M, x)
    h_prime = simplify(N - diff(psi_x, y))
    h = integrate(h_prime, y)

    psi = simplify(psi_x + h)

    print("The equation is exact.")
    print("Potential function =", psi)
    print("General solution:", psi, "= C")
else:
    print("The equation is not exact.")