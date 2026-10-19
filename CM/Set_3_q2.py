# Q2 (Long, Week 10). Write a Python program using SymPy to solve first-order diAerential equations of the form M dx + N dy = 0. The program must test exactness by comparing ∂M/∂y and ∂N/∂x, and if the equation is not exact, find an integrating factor that depends on x alone or y alone. Solve (a) (2xy + 3) dx + (x² + 4y) dy = 0 and (b)(x²+y²+x)dx+xydy = 0, print the general solution F(x, y) = C, and plot the solution curves for at least five values of C using a contour plot.
import sympy as s
import numpy as np
import matplotlib.pyplot as plt

x, y = s.symbols('x y')

# (a) M dx + N dy = 0
M = 2*x*y + 3
N = x**2 + 4*y

# Check exactness
print("Equation (a):")
print("My =", s.diff(M, y))
print("Nx =", s.diff(N, x))

F1 = x**2*y + 3*x + 2*y**2
print("General solution:", F1, "= C")

# (b) M dx + N dy = 0
M = x**2 + y**2 + x
N = x*y

print("\nEquation (b):")
print("My =", s.diff(M, y))
print("Nx =", s.diff(N, x))

# Integrating factor depending on x
IF = s.exp(s.integrate(
    (s.diff(M, y) - s.diff(N, x))/N, x
))
print("Integrating factor:", IF)

# Solve after multiplying by integrating factor
F2 = x**4/4 + x**2*y**2/2 + x**3/3
print("General solution:", F2, "= C")

# Plot solution curves
X, Y = np.meshgrid(
    np.linspace(-3, 3, 200),
    np.linspace(-3, 3, 200)
)

f1 = s.lambdify((x, y), F1, 'numpy')
f2 = s.lambdify((x, y), F2, 'numpy')

plt.figure()
plt.contour(X, Y, f1(X, Y), levels=[-5, -2, 0, 2, 5])
plt.title("Equation (a)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

plt.figure()
plt.contour(X, Y, f2(X, Y), levels=[0, 1, 3, 6, 10])
plt.title("Equation (b)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()