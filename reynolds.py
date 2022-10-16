import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def eqn(f, E, Re):
    return -2 * np.sqrt(f) * np.log10(E / 3.8 + 2.51 / (Re * np.sqrt(f))) - 1

def plot_reynolds():
    E_values = np.logspace(-6, -1, 12)
    array = np.logspace(3.47713, 8, 100)

    for E in E_values:
        friction_factors = []
        for number in array:
            Re = number
            sol = root(lambda f: eqn(f, E, Re), 0.001)
            friction_factors.append(sol.x[0])
        plt.plot(array, friction_factors, lw=2, label=f'E = {E}')

    laminar = np.logspace(2.5, 3.47712, 100)
    ff_laminar = 64 / laminar
    plt.plot(laminar, ff_laminar, lw=2)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel('Reynolds Number', fontsize=18)
    plt.ylabel('Friction Factor', fontsize=18)
    plt.legend(bbox_to_anchor=(1, 1), ncol=1)
    plt.grid(True, which="both", ls="-")
    plt.show()