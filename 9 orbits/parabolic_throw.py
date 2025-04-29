import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def xDerivative(x, t):
    return 12

def yDerivative(y, t):
    return -9.8 * t + 10

t_max = 1.8
dt = 0.0001
t = np.arange(0, t_max, dt)

x0 = 0
y0 = 0

eval_x = spi.odeint(xDerivative, x0, t)
eval_y = spi.odeint(yDerivative, y0, t)
plt.plot(eval_x, eval_y)
plt.title('Parabolic Throw')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.xlim(0, 12)
plt.ylim(0, 10)
plt.grid()
plt.show()

print("Final position: (", round(float(eval_x[-1]), 3), ",", round(float(eval_y[-1]),3), ")")