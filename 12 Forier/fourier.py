import cmath
import math

def fft(A):
    N = len(A)
    # require power-of-two length
    if N & (N-1):
        raise ValueError("Length of A must be a power of two")
    if N == 1:
        return A

    # split and recurse
    even = fft(A[0::2]) # even-indexed elements
    odd  = fft(A[1::2]) # odd-indexed elements

    out = [0]*N
    for k in range(N//2):
        # twiddle factor e^(−2πik/N)
        t = cmath.exp(-2j*math.pi*k/N) * odd[k]
        out[k]           = even[k] + t
        out[k + N//2]    = even[k] - t
    return out

A = [3, 3, 7, 3, 7, 2, 8, 6]
R = fft(A)
last = R[-1]
print(f"Last element: {last.real:.6f}{last.imag:+.6f}j")
