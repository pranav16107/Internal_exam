# Q1 (Short, Week 3). Write a Python program that generates a random 3×3 integer matrix (entries from 1to 9), computes its eigenvalues and eigenvectors, and verifies Av = λv for each eigenpair by printing the residual.

#Residual = Av-λv A means martix a v=>?eigen vectors 

import numpy as np

A = np.random.randint(1, 10, (3, 3))
values, vectors = np.linalg.eig(A)

print("Matrix A:\n", A)
print("\nEigenvalues:\n", values)

for i in range(3):
    v = vectors[:, i] # ':'=>colon means selects all rows.
    residual = A @ v - values[i] * v
    print(f"\nEigenvector {i+1}:\n", v)
    print("Residual:", residual)
