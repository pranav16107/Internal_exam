    # Graph of the function
x = np.linspace(1, 4, 100)
plt.plot(x, f(x))
plt.plot(c, f(c), 'ro')
plt.grid()
plt.show()

# Convergence graph
plt.plot(iterations, roots, 'o-')
plt.grid()
plt.show()