
# Program to obtain a matrix from a quadratic form

import sympy as sp

# Define the variables
x, y, z = sp.symbols('x y z')

# Given quadratic form
Q = x**2 + y**2 + z**2 + 2*x*y

# Obtain the matrix by taking half of the Hessian
A = sp.hessian(Q, (x, y, z)) / 2

# Display the matrix
print("Matrix of the quadratic form:")
print(A)
