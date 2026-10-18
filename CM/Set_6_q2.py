# Q2 (Long, Week 11). A cup of coAee at 90 °C is placed in a room at 25 °C and cools to 70 °C in 10 minutes. Write a Python program using SymPy to solve Newton's law of cooling dT/dt = −k(T − 25), determine the constant k from the given data, find the temperature after 30 minutes and the time taken to reach 40 °C. Plot T(t) for 0 to 60 minutes with the room temperature shown as a dashed line and the computed points marked

import sympy as s
import numpy as np
import matplotlib.pyplot as plt

t, k = s.symbols('t k')

# Temperature formula
T = 25 + 65 * s.exp(-k*t)

# Find k when T(10) = 70
kval = s.solve(T.subs(t, 10) - 70, k)[0]
print("k =", s.N(kval))

# Temperature after 30 minutes
T30 = T.subs(k, kval).subs(t, 30)
print("Temperature after 30 min =", s.N(T30))

# Time to reach 40 degrees
time = s.solve(T.subs(k, kval) - 40, t)[0]
print("Time to reach 40°C =", s.N(time))

# Plot graph
f = s.lambdify(t, T.subs(k, kval), 'numpy')
x = np.linspace(0, 60, 100)

plt.plot(x, f(x))
plt.axhline(25, linestyle='--')
plt.scatter([0, 10, 30, float(time)], [90, 70, float(T30), 40])
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()