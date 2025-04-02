import numpy as np
import matplotlib.pyplot as plt

# Updated data
U_a = np.array([350, 400, 450, 500, 550, 420])  # Acceleration voltage
B2 = np.array([3.29395E-05, 3.69422E-05, 4.1902E-05, 4.5382E-05, 4.92646E-05, 3.87948E-05])
dB2 = np.array([5.80165E-10, 6.07636E-10, 6.41676E-10, 6.6556E-10, 6.92208E-10, 6.20351E-10])

# Weighted linear regression
w = 1 / dB2**2
W = np.sum(w)
x_mean = np.sum(w * U_a) / W
delta = np.sum(w * (U_a - x_mean)**2)

slope = np.sum(w * (U_a - x_mean) * B2) / delta
intercept = np.sum(w * (B2 - slope * U_a)) / W
slope_error = np.sqrt(1 / delta)

# Print results
print(f"Slope: {slope:.3e} ± {slope_error:.2e}")
print(f"Intercept: {intercept:.3e}")

# Plot
plt.errorbar(U_a, B2, yerr=dB2, fmt='o', label='Data with error bars', capsize=3)
plt.plot(U_a, slope * U_a + intercept, label='Linear Fit', color='orange')
plt.xlabel('Acceleration Voltage $U_a$ (V)')
plt.ylabel('$B^2$ [V²/m²]')
plt.title('Linear Fit of $B^2$ vs. $U_a$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
