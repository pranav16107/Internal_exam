
# Program to solve linear equations using Gauss-Seidel Method

# Given equations:
# 10x + y + z = 12
# 2x + 10y + z = 13
# 2x + 2y + 10z = 14

# Initial values
x = 0
y = 0
z = 0

# Number of iterations
n = 10

print("Iteration\t x\t\t y\t\t z")

for i in range(1, n + 1):

    # Calculate new values using Gauss-Seidel Method
    x = (12 - y - z) / 10
    y = (13 - 2*x - z) / 10
    z = (14 - 2*x - 2*y) / 10

    # Display values after each iteration
    print(i, "\t\t", round(x, 4),
          "\t", round(y, 4),
          "\t", round(z, 4))

# Display final solution
print("\nApproximate solution:")
print("x =", round(x, 4))
print("y =", round(y, 4))
print("z =", round(z, 4))
