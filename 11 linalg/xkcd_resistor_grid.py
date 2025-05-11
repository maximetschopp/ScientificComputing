import numpy as np


def create_grid(n):
    G = np.zeros((n*n,n*n))
    for i in range(0, n * n):
        G[i][i] = 4
        # cell left
        G[i + n - 1 if i % n == 0 else i - 1][i] = -1
        # cell right
        G[ i - (n - 1) if i % n == n - 1 else i + 1][i] = -1
        # cell above 
        G[(n - 1) * n + i % n if i // n == 0 else i - n][i] = -1
        # cell below
        G[i % n if i // n == n - 1 else i + n][i] = -1
    return G

n = 5
G = create_grid(n)

I = np.zeros(n * n)
I[0] = 1       # current source
I[-1] = -1     # current sink

V = np.linalg.solve(G, I)

print(V)
