
# Program to solve a non-homogeneous ODE

import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')

# Define the differential equation: y'' - y = e^x
eq = sp.Eq(sp.diff(y(x), x, 2) - y(x), sp.exp(x))

# Solve the differential equation
solution = sp.dsolve(eq, y(x))

# Display the equation and solution
print("Given differential equation:")
sp.pprint(eq)

print("\nGeneral solution:")
sp.pprint(solution)
