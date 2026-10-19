# Q2 (Long, Weeks 6&7). Write a Python program to find a real root of f(x) = x³ − 2x − 5 using the Newton-Raphson method with initial guess x₀ = 2 and tolerance 10⁻⁶. The program must take f and f′ as functions, stop if f′(x) = 0 with a message, print a table of  iteration number, xₙ, f(xₙ) and error, and stop at tolerance or after 50 iterations. Plot f(x) with the tangent lines of the first three iterations, and plot the error against the iteration number on a log scale. Run the same program for x·eˣ − 2 = 0 with x₀ = 1 and compare the number of iterations. 


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

def newton(f, x0):
    df = sp.diff(f, x)
    f = sp.lambdify(x, f, 'numpy')
    df = sp.lambdify(x, df, 'numpy')

    errors = []
    xn = x0

    print("\nn\t x_n\t\t Error")

    for n in range(1, 51):
        if df(xn) == 0:
            print("Derivative is zero")
            break

        xnew = xn - f(xn) / df(xn)
        error = abs(xnew - xn)

        print(n,"\t",round(xnew, 6),"\t\t",round(error, 8))
        errors.append(error)
        xn = xnew

        if error < 1e-6:
            break

    print("Root =", round(xn, 6))
    print("Iterations =", len(errors))

    # Error graph
    plt.plot(range(1, len(errors)+1), errors, 'o-',
             label="Error")
    plt.yscale('log')
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.title("Newton-Raphson Error Graph")
    plt.grid()
    plt.legend()
    plt.show()

    return len(errors)


# First equation
f1 = x**3 - 2*x - 5
n1 = newton(f1, 2)

# Second equation
f2 = x * sp.exp(x) - 2
n2 = newton(f2, 1)

print("Iteration comparison:", n1, n2)
