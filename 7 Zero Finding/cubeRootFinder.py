import numpy as np

# x^3 + x - 67
cubedCoefficient = 1
squaredCoefficient = 0
linearCoefficient = 1
constantTerm = -67

f_x = [cubedCoefficient, squaredCoefficient, linearCoefficient, constantTerm]
f_prime_x = [0, cubedCoefficient * 3, squaredCoefficient * 2, linearCoefficient * 1]

commonCubes = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3]

epsilon = 1E-10

def f(x, a):
    return a[0] * x**3 + a[1] * x**2 + a[2] * x + a[3]
 
def solveCubeRoot():
    # find the closest term to the constant term as a starting point
    x = float(sorted(commonCubes, key=lambda cube: abs(cube - abs(f_x[3])))[0]) * np.sign(f_x[3])
    delta_X = 1
    count = 0
    print(x)
    while abs(delta_X) > epsilon:
        x = x - f(x, f_x) / f(x, f_prime_x)
        delta_X = f(x, f_x)
        count += 1
    print("Iterations: ", count)
    return x

print(solveCubeRoot())