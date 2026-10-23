
# Newton's Law of Cooling and Exponential Growth/Decay

import math

# -------- Newton's Law of Cooling --------

T0 = 100       # Initial temperature
Ts = 25        # Surrounding temperature
k = 0.1        # Cooling constant
t = 10         # Time in minutes

T = Ts + (T0 - Ts) * math.exp(-k * t)

print("NEWTON'S LAW OF COOLING")
print("Temperature after", t, "minutes =", round(T, 2))


# -------- Exponential Growth --------

P0 = 100       # Initial quantity
k = 0.2        # Growth constant
t = 5          # Time

P_growth = P0 * math.exp(k * t)

print("\nEXPONENTIAL GROWTH")
print("Quantity after growth =", round(P_growth, 2))


# -------- Exponential Decay --------

k = 0.2        # Positive decay constant

P_decay = P0 * math.exp(-k * t)

print("\nEXPONENTIAL DECAY")
print("Quantity after decay =", round(P_decay, 2))
