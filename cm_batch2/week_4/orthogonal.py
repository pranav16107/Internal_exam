# Program to orthogonalize a matrix using Gram-Schmidt

import sympy as sp

# Step 1: Enter the given matrix
A = sp.Matrix([[1, 1, 0],
               [1, 0, 1],
               [0, 1, 1]])

print("Original Matrix:")
sp.pprint(A)

# Step 2: Get the columns of the matrix
vectors = A.columnspace()

# Step 3: Apply Gram-Schmidt and normalize the vectors
vectors = sp.GramSchmidt(vectors, True)

# Step 4: Combine the vectors into a matrix
P = sp.Matrix.hstack(*vectors)

print("\nOrthogonalized Matrix:")
sp.pprint(P)

# Step 5: Verify that P transpose multiplied by P is identity
print("\nVerification (P transpose * P):")
sp.pprint(sp.simplify(P.T * P))

# Step 6: Check whether the matrix is orthogonal
if sp.simplify(P.T * P) == sp.eye(3):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
