# Q1 (Short, Week 2). Write a Python program to solve the non-homogeneous system x + y 
# + z = 6, 2x − y + z = 3, x + 2y − z = 2. Compare the rank of the coeAicient matrix with the 
# rank of the augmented matrix, state the type of solution (unique, infinite or none) and 
# print the solution.

import numpy as np

A = np.array([[1, 1, 1],
              [2, -1, 1],
              [1, 2, -1]], dtype=float)

B = np.array([6, 3, 2], dtype=float)

# Calculate rank
rank_A = np.linalg.matrix_rank(A)
rank_AB = np.linalg.matrix_rank(np.column_stack((A, B)))

print("Rank of A:", rank_A)
print("Rank of augmented matrix:", rank_AB)

# Find the type of solution
if rank_A != rank_AB:
    print("No solution")
elif rank_A < A.shape[1]:
    print("Infinite solutions")
else:
    print("Unique solution")

    # Solve
    x = np.linalg.solve(A, B)

    print("Solution:")
    print(f"x = {x[0]:.2f}")
    print(f"y = {x[1]:.2f}")
    print(f"z = {x[2]:.2f}")