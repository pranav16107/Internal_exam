
# Homogeneous linear equations
# x + y + z = 0
# 2x + 2y + 2z = 0
# x - y = 0

import sympy as sp

A = sp.Matrix([[1, 1, 1],
               [2, 2, 2],
               [1, -1, 0]])

print("Rank =", A.rank())
print("Determinant =", A.det())

if A.rank() == 3:
    print("Only trivial solution exists")
else:
    print("Non-trivial solutions also exist")

print("Trivial solution: x=0, y=0, z=0")
