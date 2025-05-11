import numpy as np

def create_grid(n):
    N = n * n
    G = np.zeros((N, N))

    for i in range(N):
        row = i // n
        col = i % n

        G[i][i] = 4

        # LEFT neighbor (wrap around if col == 0)
        left = row * n + ((col - 1) % n)
        G[i][left] = -1

        # RIGHT neighbor (wrap around if col == n-1)
        right = row * n + ((col + 1) % n)
        G[i][right] = -1

        # UP neighbor (wrap around if row == 0)
        up = ((row - 1) % n) * n + col
        G[i][up] = -1

        # DOWN neighbor (wrap around if row == n-1)
        down = ((row + 1) % n) * n + col
        G[i][down] = -1

    return G

n = 50
# Build full G and I
G = create_grid(n)
I = np.zeros(n * n)
I[0] = 1
I[-1] = -1

# Ground one node to make system solvable
G_reduced = G[:-1, :-1]
I_reduced = I[:-1]

# Solve
V_reduced = np.linalg.solve(G_reduced, I_reduced)

# Append grounded node
V = np.append(V_reduced, 0)

joined = ""

for i, v in enumerate(V):
    joined += str(round(v, 2)) + ", " if i < len(V) else ""
print(joined)

# Get equivalent resistance
R = V[0] - V[-1]
print("Equivalent resistance:", R)
