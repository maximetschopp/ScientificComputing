import numpy as np
import matplotlib.pyplot as plt

def plotHalleys (psi_0, psi_1):
    psi_intervals = np.linspace(psi_0, psi_1, 100)
    a = 17.8 # [Au]
    e = 0.967 # eccentricity set
    x = [a * (np.cos(psi) - e) for psi in psi_intervals ]
    y = [a * (1 - e**2) ** 0.5 * np.sin(psi) for psi in psi_intervals]
    plt.axis('equal')
    plt.title("Halley's Comet Orbit")
    plt.xlabel('x [AU]')
    plt.ylabel('y [AU]')
    plt.plot(x,y)
    plt.show()

plotHalleys(0 , 2 * np.pi)

def plotOumuamua (psi_0, psi_1):
    psi_intervals = np.linspace(psi_0, psi_1, 100)
    a = 1.28 # [Au]
    e = 1.2 # eccentricity set
    x = [a * (e - np.cosh(psi)) for psi in psi_intervals ]
    y = [a * (e**2 - 1) ** 0.5 * np.sinh(psi) for psi in psi_intervals]
    plt.axis('equal')
    plt.title("Oumuamua's Hyperbolic Orbit")
    plt.xlabel('x [AU]')
    plt.ylabel('y [AU]')
    plt.plot(x,y)
    plt.show()

plotOumuamua(-4 , 4)