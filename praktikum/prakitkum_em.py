import numpy as np
import matplotlib.pyplot as plt

# Data
U_a = np.array([350, 400, 450, 500, 550, 420])  # Acceleration voltage
dU_a = np.full_like(U_a, 5)  # Error in acceleration voltage

B2 = np.array([3.29395E-05, 3.69422E-05, 4.1902E-05, 4.5382E-05, 4.92646E-05, 3.87948E-05])
# New dB values
dB = np.array([2.40866E-05, 2.46503E-05, 2.53313E-05, 2.57985E-05, 2.63098E-05, 2.49068E-05])
# Propagate error: if B² = (B)², then d(B²) = 2 * B * dB
dB2 = 2 * np.sqrt(B2) * dB

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
plt.errorbar(U_a, B2, xerr=dU_a, yerr=dB2, fmt='o', label='Data with error bars', capsize=3)
plt.plot(U_a, slope * U_a + intercept, label='Linear Fit', color='orange')
plt.xlabel('Acceleration Voltage $U_a$ (V)')
plt.ylabel('$B^2$ [V²/m²]')
plt.title('Linear Fit of $B^2$ vs. $U_a$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
