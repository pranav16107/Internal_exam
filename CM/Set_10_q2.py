# Q2 (Long, Weeks 1&2). Write a menu-driven Python program that solves AX = B for homogeneous (B = 0) and non-homogeneous systems by comparing the rank of A with the rank of the augmented matrix [A|B]. The program must report one of: only the trivial solution, non-trivial (infinitely many) solutions, a unique solution, infinitely many  solutions, or inconsistent. Test it on (a) x + y + z = 0, 2x − y + 3z = 0, 3x + 4z = 0; (b) x + y + z  = 3, x + 2y + 3z = 6, 2x + y + z = 4; (c) x + y + z = 3, 2x + 2y + 2z = 6, x − y + z = 1; (d) x + y + z =3, x + y + z = 4, x − y = 0. For case (b), plot the three planes in 3D and mark their point of intersection.

import numpy as np
import matplotlib.pyplot as plt

cases = [
    ([[1,1,1], [2,-1,3], [3,0,4]], [0,0,0]),
    ([[1,1,1], [1,2,3], [2,1,1]], [3,6,4]),
    ([[1,1,1], [2,2,2], [1,-1,1]], [3,6,1]),
    ([[1,1,1], [1,1,1], [1,-1,0]], [3,4,0])
]

for i, (A, B) in enumerate(cases):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    r1 = np.linalg.matrix_rank(A)
    r2 = np.linalg.matrix_rank(np.column_stack((A, B)))

    print("\nCase", chr(97+i))
    print("Rank of A:", r1)
    print("Rank of [A|B]:", r2)

    if r1 != r2:
        print("Inconsistent: No solution")
    elif r1 < A.shape[1]:
        if np.all(B == 0):
            print("Non-trivial infinitely many solutions")
        else:
            print("Infinitely many solutions")
    elif np.all(B == 0):
        print("Only the trivial solution")
    else:
        print("Unique solution:", np.linalg.solve(A, B))

# Plot the three planes for case (b)
x, y = np.meshgrid(np.linspace(-2, 5, 30),
                   np.linspace(-2, 5, 30))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, 3-x-y, alpha=0.4)
ax.plot_surface(x, y, (6-x-2*y)/3, alpha=0.4)
ax.plot_surface(x, y, 4-2*x-y, alpha=0.4)

ax.scatter(1, 1, 1, color='red', s=50)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()