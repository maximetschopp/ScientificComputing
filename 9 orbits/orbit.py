import numpy as np
import matplotlib.pyplot as plt

dt = 600.0
T_total = 3600.0 * 24 * 8
steps = int(T_total / dt)

data = np.loadtxt('/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/9 orbits/gliese876ini.txt')
M = data[:, 0]
R = data[:, 1:3].copy()
V = data[:, 3:5].copy()
N = len(M)

Rs = np.zeros((steps + 1, N, 2))
Es = np.zeros(steps + 1)
Rs[0] = R.copy()

def accelerations(R):
    acc = np.zeros_like(R)
    for k in range(N):
        diff = R[k] - R
        dist = np.linalg.norm(diff, axis=1)
        dist3 = dist**3
        dist3[dist3 == 0] = np.inf
        acc[k] = -np.sum((M[:, None] * diff) / dist3[:, None], axis=0)
    return acc

def energy(R, V):
    kin = 0.5 * np.sum(M * np.sum(V**2, axis=1))
    pot = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            rij = np.linalg.norm(R[i] - R[j])
            pot -= M[i] * M[j] / rij
    return kin + pot

acc = accelerations(R)
V_half = V + 0.5 * acc * dt
V_full = V_half - 0.5 * acc * dt
Es[0] = energy(R, V_full)

for i in range(1, steps + 1):
    R += V_half * dt
    acc = accelerations(R)
    V_half += acc * dt
    Rs[i] = R.copy()
    V_full = V_half - 0.5 * acc * dt
    Es[i] = energy(R, V_full)

plt.figure(figsize=(8, 8))
for k in range(1, N):
    plt.plot(Rs[:, k, 0], Rs[:, k, 1], label=f'Planet {k}')
plt.scatter(0, 0, s=10, label='Star (COM)')
plt.gca().set_aspect('equal')
plt.xlabel('X (light-seconds)')
plt.ylabel('Y (light-seconds)')
plt.legend()
plt.title('Gliese 876 Orbits')
plt.show()

times = np.arange(steps + 1) * dt
plt.figure()
plt.plot(times / 3600, (Es - Es[0]) / Es[0])
plt.xlabel('Time (hours)')
plt.ylabel('Relative Energy Error')
plt.title('Energy Conservation')
plt.grid(True)
plt.show()
