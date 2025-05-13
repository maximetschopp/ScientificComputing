import numpy as np

def solve_lineqs_grounded(A, b, ground_index=0):
    '''
    Solves A @ x = b for x by grounding one node (removing row and column at ground_index).
    A must be symmetric and singular (e.g., a Laplacian).
    '''
    A_reduced = np.delete(A, ground_index, axis=0)
    A_reduced = np.delete(A_reduced, ground_index, axis=1)
    b_reduced = np.delete(b, ground_index, axis=0)

    x_reduced = np.linalg.solve(A_reduced, b_reduced)

    # Insert 0V at grounded node
    x = np.insert(x_reduced, ground_index, 0)
    return x

def is_neighbor(i, j, N):
    # Check if nodes i and j are adjacent in a flat N x N grid
    xi, yi = i % N, i // N
    xj, yj = j % N, j // N
    return abs(xi - xj) + abs(yi - yj) == 1

def get_connections(i, N):
    # Returns number of neighbors (between 2 and 4)
    x, y = i % N, i // N
    connections = 4
    if x == 0 or x == N-1:
        connections -= 1
    if y == 0 or y == N-1:
        connections -= 1
    return connections

def resistance(N):
    size = N * N
    A = np.zeros((size, size))

    # Build Laplacian
    for i in range(size):
        A[i, i] = get_connections(i, N)
        for j in range(size):
            if i != j and is_neighbor(i, j, N):
                A[i, j] = -1

    # Inject current between two interior nodes
    source_x, source_y = N // 2 + 1, N // 2
    sink_x, sink_y = N // 2 - 1, N // 2 - 1
    source = source_y * N + source_x
    sink = sink_y * N + sink_x

    I = np.zeros((size, 1))
    I[source] = 1
    I[sink] = -1

    V = solve_lineqs_grounded(A, I)
    return float(V[source] - V[sink])

# Example usage
for N in range(5, 60, 5):
    print(f"N = {N}, Resistance ≈ {resistance(N):.5f}")
