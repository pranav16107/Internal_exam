# Q2 (Long, Week 12). Write a Python program using SymPy to solve homogeneous second-order linear ODEs with constant coeAicients: (a) y″ − 5y′ + 6y = 0, (b) y″ − 4y′ + 4y = 0, (c) y″ + 2y′ + 5y = 0. For each equation the program must compute the roots of the characteristic equation, identify the type (real distinct, repeated or complex), print  general solution, and find the particular solution for y(0) = 1, y′(0) = 0. Plot the three  the particular solutions for x from 0 to 5 on one graph with a legend.

import sympy as s
import numpy as np
import matplotlib.pyplot as plt

x = s.symbols('x')
y = s.Function('y')

eqs = [
    s.diff(y(x), x, 2) - 5*s.diff(y(x), x) + 6*y(x),
    s.diff(y(x), x, 2) - 4*s.diff(y(x), x) + 4*y(x),
    s.diff(y(x), x, 2) + 2*s.diff(y(x), x) + 5*y(x)
]

for i, eq in enumerate(eqs):
    sol = s.dsolve(eq, y(x))
    print("\nEquation", i+1)
    print("General solution:", sol)

    r = s.symbols('r')
    roots = s.solve(r**2 + [-5, -4, 2][i]*r + [6, 4, 5][i], r)
    print("Roots:", roots)

    if roots[0].is_real and roots[1].is_real:
        if roots[0] == roots[1]:
            print("Type: Repeated roots")
        else:
            print("Type: Real distinct roots")
    else:
        print("Type: Complex roots")

    p = s.dsolve(eq, y(x), ics={
        y(0): 1,
        s.diff(y(x), x).subs(x, 0): 0
    })
    print("Particular solution:", p)

    f = s.lambdify(x, p.rhs, 'numpy')
    X = np.linspace(0, 5, 100)
    plt.plot(X, f(X), label="Equation " + str(i+1))

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()