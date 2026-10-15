# Q1 (Short, Week 11). A bacterial culture of 500 cells doubles in 3 hours. Write a Python program to solve N(t) = N₀e^(kt), find k, compute the population after 10 hours and plot N(t) for 0 to 12 hours. 

import numpy as np
import matplotlib.pyplot as plt

# Initial population and growth rate
P0 = 500
k = np.log(2) / 3  # Culture doubles every 3 hours

# Calculate population after 10 hours
P10 = P0 * np.exp(k * 10)
print("Growth rate =", k)
print("Population after 10 hours =", round(P10))

# Calculate population from 0 to 12 hours
t = np.linspace(0, 12, 100)
P = P0 * np.exp(k * t)  # Exponential growth formula

# Plot the growth curve
plt.plot(t, P)
plt.xlabel("Time (hours)")
plt.ylabel("Population")
plt.title("Bacterial Growth")
plt.grid()
plt.show()