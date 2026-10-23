# Newton-Raphson Method to find a real root

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the equation
x = sp.symbols('x')
f = x**3 - x - 2
df = sp.diff(f, x)

# Convert equation and derivative into functions
F = sp.lambdify(x, f, 'numpy')
DF = sp.lambdify(x, df, 'numpy')

# Initial guess and accuracy
a = 1.5
e = 0.0001

# Find the root
while abs(F(a)) > e:
    a = a - F(a) / DF(a)

print("Approximate root =", round(a, 4))


# Draw the graph
x1 = np.linspace(0, 2.5, 100)

plt.plot(x1, F(x1), label="y = x^3 - x - 2")
plt.axhline(0, color="black")
plt.plot(a, F(a), 'ro', label="Root")

plt.title("Newton-Raphson Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
