
# Program to check and solve an exact differential equation

import sympy as sp

x, y = sp.symbols('x y')

# Define M and N
M = 2*x*y + 3
N = x**2 + 4*y

# Calculate partial derivatives
dM_dy = sp.diff(M, y)
dN_dx = sp.diff(N, x)

print("dM/dy =", dM_dy)
print("dN/dx =", dN_dx)

# Check exactness
if sp.simplify(dM_dy - dN_dx) == 0:
    print("The equation is Exact")

    # Integrate M with respect to x
    F = sp.integrate(M, x)

    # Find the missing function of y
    g = sp.integrate(N - sp.diff(F, y), y)

    # Obtain the general solution
    F = F + g

    print("General solution:")
    sp.pprint(F)
    print("= C")

else:
    print("The equation is Non-Exact")
