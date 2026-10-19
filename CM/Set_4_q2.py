# Q2 (Long, Week 8). Write a Python program to solve the system 10x + y + z = 12, 2x + 10y + z = 13, 2x + 2y + 10z = 14 using Jacobi's iteration method. The program must check diagonal dominance, start from the initial guess (0, 0, 0), stop when the maximum change in the variables is below 10⁻⁵ or after 100 iterations, and print a table of the iterates. Verify the result with numpy.linalg.solve. Plot each variable against the iteration number and plot the residual norm on a log scale.

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[10,1,1], [2,10,1], [2,2,10]], float)
B = np.array([12,13,14], float)

dd = True

for i in range(3):
    if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(3) if i != j):
        dd = False

print("Diagonally dominant:", dd)

x = np.zeros(3)
history = [x.copy()]
residual = [np.linalg.norm(A @ x - B)]

print("Iter       x       y       z")
for i in range(1, 101):
    y = np.array([(12-x[1]-x[2])/10,
                  (13-2*x[0]-x[2])/10,
                  (14-2*x[0]-2*x[1])/10])
    change = max(abs(y-x))
    x = y
    history.append(x.copy())
    residual.append(np.linalg.norm(A @ x - B))
    print(i, np.round(x, 6))
    if change < 1e-5:
        break

print("Jacobi solution:", x)
print("NumPy solution:", np.linalg.solve(A, B))

history = np.array(history)
plt.plot(history, label=['x','y','z'])
plt.xlabel("Iteration")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()

plt.semilogy(residual, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Residual norm")
plt.grid()
plt.show()
