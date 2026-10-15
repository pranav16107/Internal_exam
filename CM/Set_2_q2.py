# Q2 (Long, Weeks 6&7). Write a Python program to find a real root of f(x) = x³ − 2x − 5 
# using the Newton-Raphson method with initial guess x₀ = 2 and tolerance 10⁻⁶. The 
# program must take f and f′ as functions, stop if f′(x) = 0 with a message, print a table of  iteration number, xₙ, f(xₙ) and error, and stop at tolerance or after 50 iterations. Plot f(x) with the tangent lines of the first three iterations, and plot the error against the iteration number on a log scale. Run the same program for x·eˣ − 2 = 0 with x₀ = 1 and compare the number of iterations. 


import numpy as np
import matplotlib.pyplot as plt

def newton(f, df, x):
    errors, tangents = [], []
    print("\nn\t x_n\t\t f(x_n)\t\t Error")

    for n in range(1, 51):
        if df(x) == 0:
            print("Derivative is zero. Stopping.")
            break

        if n <= 3:
            tangents.append((x, f(x), df(x)))

        y = x - f(x)/df(x)
        error = abs(y-x)
        print(f"{n}\t{y:.6f}\t{f(y):.6f}\t{error:.6f}")
        errors.append(error)
        x = y

        if error < 1e-6:
            break

    print("Root =", round(x, 6))
    print("Iterations =", len(errors))

    xx = np.linspace(x-1, x+1, 200)
    plt.plot(xx, f(xx))
    for a, b, m in tangents:
        plt.plot(xx, b + m*(xx-a), "--")
    plt.grid()
    plt.show()

    plt.plot(range(1, len(errors)+1), errors, "o-")
    plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.grid()
    plt.show()

    return len(errors)

f1 = lambda x: x**3 - 2*x - 5
df1 = lambda x: 3*x**2 - 2
f2 = lambda x: x*np.exp(x) - 2
df2 = lambda x: np.exp(x)*(x+1)

n1 = newton(f1, df1, 2)
n2 = newton(f2, df2, 1)

print("Iteration comparison:", n1, n2)


