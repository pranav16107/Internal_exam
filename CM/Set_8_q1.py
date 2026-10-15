# Q1 (Short, Week 9). Write a Python program to perform the first four Gauss-Seidel 
# iterations for the system 4x + y = 9, x + 3y = 7 starting from (0, 0). Print each iterate. 

def seidel(x0, y0, max_iter):
    x, y = x0, y0

    for i in range(max_iter):
        # Calculate new values using Gauss-Seidel method
        x_new = (9 - y) / 4
        y_new = (7 - x_new) / 3

        print(
            f"Iteration {i+1}: "
            f"x = {x_new:.4f}, "
            f"y = {y_new:.4f}"
        )

        # Update values
        x, y = x_new, y_new


# Initial guesses
x0 = 0
y0 = 0

# Perform first four iterations
max_iter = 4

# Call function
seidel(x0, y0, max_iter)