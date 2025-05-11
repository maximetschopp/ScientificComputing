import numpy as np

m = np.array([
    [2.0, -1.0, -1.0, 0.0],
    [-1.0, 3.0, -1.0, -1.0],
    [-1.0, -1.0, 3.0, -1.0],
    [0.0, -1.0, -1.0, 2.0]
])

I = np.array([1.0, 0.0, 0.0, -1.0])


V1 = np.linalg.solve(m, I)

print(V1)