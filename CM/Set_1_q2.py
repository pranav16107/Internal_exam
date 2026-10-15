# Q2 (Long, Weeks 4&5). Write a Python program to find a real root of f(x) = x³ − 4x − 9 in 
# the interval [2, 3] using the Bisection method with tolerance 10⁻⁴. The program must 
# check that f(a)·f(b) < 0, print a table of iteration number, a, b, c and f(c), and stop when 
# the tolerance is met or after 50 iterations. Also compute the minimum number of 
# iterations required by the formula n ≥ log₂((b − a)/tol). Plot f(x) with the root marked, and 
# plot the midpoint c against the iteration number to show convergence. 

import numpy as np
import matplotlib.pyplot as plt
import math

# Define the function
def f(x):
    return x**3 - 4*x - 9

a, b = 2, 3
tol = 0.0001
max_iter = 50

# Check whether a root exists
if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied")
else:
    print("Minimum iterations =", math.ceil(math.log2((b-a)/tol)))

    iterations, roots = [], []

    print("\nIter\t a\t\t b\t\t c\t\t f(c)")

    for i in range(1, max_iter+1):
        c = (a+b)/2
        iterations.append(i) 
        roots.append(c)# we add the values into array because it helps us to plot the graph

        print(f"{i}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}")

        # Stop when tolerance is reached
        if abs(f(c)) < tol or (b-a)/2 < tol:
            break

        # Update the interval
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    print("\nApproximate root =", c)
    print("Iterations used =", i)

    # Graph of the function
x = np.linspace(1, 4, 100)
plt.plot(x, f(x))
plt.plot(c, f(c), 'ro')# ro means red dot near c,f(c)
plt.grid()
plt.show()

# Convergence graph
plt.plot(iterations, roots, 'o-') #'o-' → draws circular markers connected by lines.
plt.grid()
plt.show()