import numpy as np

G = np.array([
    [2.0 + 1.0/0.29, -1.0/0.29, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0],
    [-1.0/0.29, 2.0 + 1.0/0.29, 0.0, -1.0, 0.0, -1.0, 0.0, 0.0],
    [-1.0, 0.0, 3.0, -1.0, 0.0, 0.0, -1.0, 0.0],
    [0.0, -1.0, -1.0, 3.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.0, 0.0, 3.0, -1.0, -1.0, 0.0],
    [0.0, -1.0, 0.0, 0.0, -1.0, 3.0, 0.0, -1.0],
    [0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 3.0, -1.0],
    [0.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, 3.0]
])

I = [ -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]

R = np.linalg.solve(G, I)

print(R[7] - R[0])