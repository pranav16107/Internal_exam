# Q1 (Short, Week 1). Write a Python program to solve the homogeneous system AX = 0 for 
# A = [[1, 2, 3], [2, 4, 6], [1, 1, 1]]. Print the rank of A, state whether the solution is trivial or 
# non-trivial, and print a basis of the null space. 

import numpy as np

A = np.array([[1, 2, 3],
              [2, 4, 6],
              [1, 1, 1]])

rank = np.linalg.matrix_rank(A)
print("Rank of A =", rank)

if rank < 3:
    print("System has a non-trivial solution")
else:
    print("System has only a trivial solution")

# Find the null space basis using SVD
U, S, V = np.linalg.svd(A)
basis = V[rank:, :].T

print("Basis of null space:")
print(basis)