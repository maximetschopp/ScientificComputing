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

I = np.array([-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])

# Eigen decomposition
eigvals, eigvecs = np.linalg.eigh(G)

# Invert eigenvalues, avoiding divide-by-zero
threshold = 1e-10
eigvals_inv = np.where(np.abs(eigvals) > threshold, 1.0 / eigvals, 0.0)

# Build pseudoinverse
G_pseudo_inv = eigvecs @ np.diag(eigvals_inv) @ eigvecs.T

# Solve
R = G_pseudo_inv @ I

# Result
print(R[7] - R[0])
