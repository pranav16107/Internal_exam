# Q2 (Long, Week 9). Write a Python program to solve the system 27x + 6y − z = 85, 6x + 15y + 2z = 72, x + y + 54z = 110 using the Gauss-Seidel method. The program must check diagonal dominance, start from (0, 0, 0), stop at tolerance 10⁻⁴ or after 100 iterations, and print the iteration table. Solve the same system with Jacobi's method and compare the number of iterations needed by the two methods. Plot the error against the iteration number for both methods on the same graph. 

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[27, 6, -1],
              [6, 15, 2],
              [1, 1, 54]], float)
B = np.array([85, 72, 110], float)

dd = True
for i in range(3):
    if abs(A[i,i]) <= sum(abs(A[i,j]) for j in range(3) if i != j):
        dd = False
print("Diagonally dominant:", dd)

def solve(jacobi):
    x = np.zeros(3)
    errors = []
    print("\nJacobi Method" if jacobi else "\nGauss-Seidel Method")
    print("Iter       x          y          z        Error")

    for i in range(1, 101):
        old = x.copy()

        if jacobi:
            x[0] = (85 - 6*old[1] + old[2]) / 27
            x[1] = (72 - 6*old[0] - 2*old[2]) / 15
            x[2] = (110 - old[0] - old[1]) / 54
        else:
            x[0] = (85 - 6*x[1] + x[2]) / 27
            x[1] = (72 - 6*x[0] - 2*x[2]) / 15
            x[2] = (110 - x[0] - x[1]) / 54

        error = max(abs(x - old))
        errors.append(error)
        print(f"{i:3d}  {x[0]:10.6f} {x[1]:10.6f} {x[2]:10.6f}  {error:.2e}")

        if error < 1e-4:
            break

    print("Iterations:", i)
    print("Solution:", x)
    return errors

gs = solve(False)
ja = solve(True)

print("\nNumPy solution:", np.linalg.solve(A, B))

plt.semilogy(range(1, len(gs)+1), gs, 'o-', label="Gauss-Seidel")
plt.semilogy(range(1, len(ja)+1), ja, 's-', label="Jacobi")
plt.xlabel("Iteration Number")
plt.ylabel("Error")
plt.title("Gauss-Seidel vs Jacobi Method")
plt.legend()
plt.grid(True)
plt.show()
