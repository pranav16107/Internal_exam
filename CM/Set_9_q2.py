# Q2 (Long, Week 12). Write a Python program using SymPy to solve the non homogeneous second-order ODEs (a) y″ − 3y′ + 2y = e³ˣ, (b) y″ + y = sin 2x and (c) y″ − 2y′ + y = x². For each equation print the complementary function, a particular integral and the general solution, and find the solution satisfying y(0) = 1, y′(0) = 0. Verify each solution by substituting it back into the equation, and plot the particular solution together with the complete solution for x from 0 to 3.

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