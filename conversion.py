import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def func(vals):
    T, c = vals

    # Constant parameters
    ci = 2
    ko = 0.01
    E = 1000
    Ti = 298
    Hr = -3 * 10 ** 4
    p = 1000
    cp = 4

    # Equations to solve
    eq1 = (1 / tau) * (ci - c) - (ko * np.exp(E / T) * c)
    eq2 = (1 / tau) * (Ti - T) - (Hr / (p * cp)) * (ko * np.exp(E / T) * c)
    return eq1, eq2

# Set up initial guesses to numerically solve problem
nums = np.logspace(0, 4, 100)
guess_T = 298
guess_c = 0.2
temperatures = []
conversions = []

for n in nums:
    tau = n
    solution = root(func, [guess_T, guess_c])
    guess_T = solution.x[0]
    guess_c = solution.x[1]
    temperatures.append(solution.x[0])
    conversions.append((2 - solution.x[1]) / 2)

plt.plot(nums, temperatures, lw=3, color='lime')
plt.xscale("log")
plt.xlabel('tau', fontsize=18)
plt.ylabel('Conversion', fontsize=18)
plt.grid(True, which="both", ls="-")
plt.show()

plt.plot(nums, conversions, lw=3, color='lime')
plt.xscale("log")
plt.xlabel('tau', fontsize=18)
plt.ylabel('T', fontsize=18)
plt.grid(True, which="both", ls="-")
plt.show()