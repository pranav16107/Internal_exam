
# Program to find eigenvalues and eigenvectors of a 3x3 matrix

import sympy as sp

# Step 1: Define the matrix given in the question
A = sp.Matrix([[1, 0, 0],
               [0, 2, 1],
               [0, 1, 2]])

# Step 2: Display the given matrix
print("Given Matrix:")
sp.pprint(A)

# Step 3: Find the eigenvalues
print("\nEigenvalues:")
print(A.eigenvals())

# Step 4: Find the eigenvectors for each eigenvalue
print("\nEigenvectors:")

for value, multiplicity, vectors in A.eigenvects():
    print("\nEigenvalue:", value)

    for vector in vectors:
        print("Eigenvector:")
        print(vector)
