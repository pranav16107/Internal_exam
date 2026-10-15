# Q1 (Short, Weeks 4&5). Write a Python program to find √2 as the root of x² − 2 = 0 in [1,2] using the Bisection method with tolerance 10⁻³. Print the root and the number of iterations taken.


def f(x):
    return x**2 - 2

a, b = 1, 2
tol = 1e-3
n = 0

while b - a > tol:
    c = (a + b) / 2
    n += 1

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root =", (a + b) / 2)
print("Iterations =", n)

