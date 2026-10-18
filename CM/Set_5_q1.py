# Q1 (Short, Week 3). Write a Python program to obtain the symmetric matrix of the  quadratic form Q = 2x² + 3y² + 4z² + 2xy − 4yz + 6xz. Print the matrix and verify that it is symmetric. 

# Generalized form of the eq is 
# Q=ax^2+by^2+cz^2+2hxy+2gxz+2fyz
# a matrix is symmetric only if Q=X^T*A*T and A=A.T;
import sympy as sp

# Define the symmetric matrix
A = sp.Matrix([
    [2, 1, 3],
    [1, 3, -2],
    [3, -2, 4]
])

# Print matrix
print("Symmetric Matrix:")
sp.pprint(A)

# Verify symmetry
print("Is symmetric?", A == A.T)
