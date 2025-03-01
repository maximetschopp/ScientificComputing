import math

epsilon = 1e-8 # 8 decimal points
initial_condition = -3 * math.pi / 4

def negative_one_power(n):
    return 1 if n % 2 == 0 else -1

def map_to_odd_number(n):
    return 2 * n + 1

def raise_to_the_nth_power(n, k):
    return math.pow(n,k)

def factorial(n):
    return math.factorial(n)

def approximate_sin(x, eps):
    total = 0
    last_term = 1
    n = 0
    while abs(last_term) > eps:
        last_term = negative_one_power(n) * raise_to_the_nth_power(x, map_to_odd_number(n)) / factorial(map_to_odd_number(n))
        total += last_term
        n+=1
    return round(total, 8)


print(approximate_sin(initial_condition, epsilon))