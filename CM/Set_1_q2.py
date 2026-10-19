# Q2 (Long, Weeks 4&5). Write a Python program to find a real root of f(x) = x³ − 4x − 9 in the interval [2, 3] using the Bisection method with tolerance 10⁻⁴. The program must check that f(a)·f(b) < 0, print a table of iteration number, a, b, c and f(c), and stop when the tolerance is met or after 50 iterations. Also compute the minimum number of iterations required by the formula n ≥ log₂((b − a)/tol). Plot f(x) with the root marked, and plot the midpoint c against the iteration number to show convergence. 


import numpy as np
import matplotlib.pyplot as plt
import math

# Define the function
def f(x):
    return x**3 - 4*x - 9

# Initial values
a, b = 2, 3
tol = 0.0001
max_iter = 50

# Check whether the Bisection method can be applied
if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied")

else:
    # Calculate minimum number of iterations
    n = math.ceil(math.log2((b - a) / tol))
    print("Minimum iterations =", n)

    iterations = []
    roots = []

    print("\nIter\t a\t\t b\t\t c\t\t f(c)")

    # Bisection method
    for i in range(1, max_iter + 1):
        c = (a + b) / 2

        iterations.append(i)
        roots.append(c)

        print(f"{i}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}")

        # Check stopping condition
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break

        # Update the interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nApproximate root =", c)
    print("Iterations used =", i)

    # Graph 1: Function and approximate root
    x = np.linspace(1, 4, 100)

    plt.plot(x, f(x), label="f(x) = x^3 - 4x - 9")
    plt.plot(c, f(c), 'ro', label="Approximate root")
    plt.axhline(y=0, label="X-axis (y = 0)")

    plt.xlabel("x values")
    plt.ylabel("f(x)")
    plt.title("Bisection Method - Function and Root")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Graph 2: Convergence graph
    plt.plot(iterations, roots, 'o-', label="Midpoint c")

    plt.xlabel("Iteration Number")
    plt.ylabel("Midpoint (c)")
    plt.title("Bisection Method - Convergence Graph")
    plt.grid(True)
    plt.legend()
    plt.show()
