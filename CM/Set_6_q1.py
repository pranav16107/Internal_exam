# Q1 (Short, Weeks 6&7). Write a Python program to find the cube root of 10 using the 
# Newton-Raphson method on f(x) = x³ − 10 with x₀ = 2 and tolerance 10⁻⁶. Print the root  and the number of iterations. 

x = 2
tol = 1e-6
iterations = 0

while True:
    f = x**3 - 10
    df = 3*x**2
    x_new = x - f/df
    iterations += 1

    if abs(x_new - x) < tol:
        x = x_new
        break

    x = x_new

print("Approximate root =", x)
print("Number of iterations =", iterations)