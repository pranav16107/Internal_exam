# Q1 (Short, Week 2). Write a Python program to solve the non-homogeneous system x + y + z = 6, 2x − y + z = 3, x + 2y − z = 2. Compare the rank of the coeAicient matrix with the rank of the augmented matrix, state the type of solution (unique, infinite or none) and print the solution.

import sympy as sp

A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
B = sp.Matrix([6, 3, 2])

r1 = A.rank()
r2 = A.row_join(B).rank()

print("Rank of A:", r1)
print("Rank of augmented matrix:", r2)

if r1 != r2:
    print("No solution")
elif (r1==r2) and (r1<3):
    print("Infinite solutions")
else:
    print("Unique solution")
    print("Solution:", A.inv() * B) #AX=B => X=A⁻¹*B