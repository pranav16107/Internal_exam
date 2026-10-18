# Q2 (Long, Week 3). Write a Python program that generates a symmetric 3×3 matrix dynamically (from user input or random integers), computes its eigenvalues and eigenvectors, verifies that QᵀQ = I for the matrix Q of eigenvectors, and diagonalises the matrix as A = QΛQᵀ. Then apply Gram-Schmidt orthogonalisation to the columns of a given 3×3 matrix and verify the result. For a 2×2 symmetric matrix, plot the eigenvectors as arrows together with the unit circle and its image under A.

import numpy as np
import matplotlib.pyplot as plt

# Symmetric matrix
A = np.array([[2, 1, 0],
              [1, 2, 1],
              [0, 1, 2]])

# Eigenvalues and eigenvectors
L, Q = np.linalg.eigh(A)
print("Eigenvalues:", L)
print("Eigenvectors:\n", Q)
print("Q.T @ Q:\n", Q.T @ Q)
print("A = QLQ.T:\n", Q @ np.diag(L) @ Q.T)

# Gram-Schmidt
B = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 1]])

G, R = np.linalg.qr(B)
print("Gram-Schmidt:\n", G)
print("Verification:\n", G.T @ G)

# 2x2 matrix plot
A = np.array([[2, 1], [1, 2]])
L, Q = np.linalg.eigh(A)
t = np.linspace(0, 2*np.pi, 100)
C = np.array([np.cos(t), np.sin(t)])
D = A @ C

plt.plot(C[0], C[1], label="Unit Circle")
plt.plot(D[0], D[1], label="Image")
for i in range(2):
    plt.quiver(0, 0, Q[0,i], Q[1,i], angles='xy', scale_units='xy', scale=1)
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()