# Q1 (Short, Week 8). Write a Python program to perform the first five Jacobi iterations for the system 5x − y = 9, −x + 5y = 7 starting from (0, 0). Print each iterate.


def jacobi(x0, y0, max_iter):
    x, y = x0, y0

    for i in range(max_iter):
        x_new = (9 + y) / 5
        y_new = (7 + x) / 5

        print(f"Iteration {i+1}: x = {x_new:.4f}, y = {y_new:.4f}")

        x, y = x_new, y_new

# Initial guesses
x0 = 0
y0 = 0

# Perform first five iterations
max_iter = 5

jacobi(x0, y0, max_iter)