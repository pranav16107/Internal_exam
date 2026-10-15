# Q2 (Long, Weeks 4&5). Write a Python program to find a real root of f(x) = x³ − 4x − 9 in 
# the interval [2, 3] using the Bisection method with tolerance 10⁻⁴. The program must 
# check that f(a)·f(b) < 0, print a table of iteration number, a, b, c and f(c), and stop when 
# the tolerance is met or after 50 iterations. Also compute the minimum number of 
# iterations required by the formula n ≥ log₂((b − a)/tol). Plot f(x) with the root marked, and 
# plot the midpoint c against the iteration number to show convergence. 

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**3 - 4*x - 9

a = 2
b = 3
tol = 1e-4
max_iter = 50

# Check sign change
if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied")
else:
    # Minimum number of iterations
    n = math.ceil(math.log2((b - a) / tol))
    print("Minimum number of iterations =", n)

    iterations = []
    roots = []

    print("\nIt\t a\t\t b\t\t c\t\t f(c)")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2

        iterations.append(i)
        roots.append(c)

        print(f"{i}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}")

        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nApproximate root =", c)
    print("Number of iterations =", i)

    # Plot the function
    x = np.linspace(1, 4, 400)
    y = f(x)

    plt.plot(x, y, label="f(x) = x^3 - 4x - 9")
    plt.axhline(0, color="black")
    plt.scatter(c, f(c), label="Approximate root")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method")
    plt.legend()
    plt.grid()
    plt.show()

    # Plot convergence
    plt.plot(iterations, roots, marker="o")
    plt.xlabel("Iteration number")
    plt.ylabel("Midpoint c")
    plt.title("Convergence of Bisection Method")
    plt.grid()
    plt.show()