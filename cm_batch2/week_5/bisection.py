
# Bisection Method to find a real root and draw graph

import matplotlib.pyplot as plt
import numpy as np

# Define the equation
def f(x):
    return x**3 - x - 2

# Initial values
a = 1
b = 2
e = 0.0001

# Check the interval
if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied")

else:
    # Find the root
    while (b - a) / 2 > e:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    print("Approximate root =", round(root, 4))

    # Draw the graph
    x = np.linspace(0, 2.5, 100)
    plt.plot(x, f(x))
    plt.axhline(0)
    plt.plot(root, f(root), 'o', label="Approximate root")
    plt.grid()
    plt.show()
