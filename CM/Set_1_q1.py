# Q1 (Short, Week 1). Write a Python program to solve the homogeneous system AX = 0 for 
# A = [[1, 2, 3], [2, 4, 6], [1, 1, 1]]. Print the rank of A, state whether the solution is trivial or non-trivial, and print a basis of the null space. 

import sympy as sp

A = sp.Matrix([[1, 2, 3],
               [2, 4, 6],
               [1, 1, 1]])# sp.matrix creates the mathematical matrix 

print("Rank =", A.rank()) #A.rank() helps in finding the rank of the matrix 

if A.rank() < A.cols:#a.cols give the no of cols in the matrix 
    print("Non-trivial solution")
else:
    print("Only trivial solution")

print("Null space basis =", A.nullspace())