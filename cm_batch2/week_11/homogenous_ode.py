
# Program to solve a homogeneous first-order ODE

import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')

# Define the differential equation
eq = sp.Eq(sp.diff(y(x), x), 1 + y(x)/x)

# Solve the differential equation
solution = sp.dsolve(eq, y(x))

# Display the solution
print("Given differential equation:")
sp.pprint(eq)

print("\nGeneral solution:")
sp.pprint(solution)
