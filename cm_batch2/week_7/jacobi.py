
# Program to solve linear equations using Jacobi Method

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

    # Calculate new values using previous values
    x1 = (12 - y - z) / 10
    y1 = (13 - 2*x - z) / 10
    z1 = (14 - 2*x - 2*y) / 10

    # Display the values
    print(i, "\t\t", round(x1, 4),
          "\t", round(y1, 4),
          "\t", round(z1, 4))

    # Update values for the next iteration
    x = x1
    y = y1
    z = z1

# Display final solution
print("\nApproximate solution:")
print("x =", round(x, 4))
print("y =", round(y, 4))
print("z =", round(z, 4))
