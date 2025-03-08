import numpy as np
from fractions import Fraction

def generateFactorials (N):
    a = [1]
    for i in range(N):
        a.append(a[i] * (i + 1))
    print (a)
    return a

def bernoulliNum (N):
    factorials = np.array(generateFactorials(N + 1))
    bernoulli_numbers = [1]

    for n in range(1, N + 1):
        sum = Fraction(0)
        for k in range (n):
            numerator = factorials[n] * bernoulli_numbers[k]
            denominator = factorials[k] * factorials[ n - k + 1]
            print(n,k, "     ",numerator, denominator)
            sum -= Fraction(numerator=numerator, denominator=denominator)
        print('-'*20)
        bernoulli_numbers.append(sum)

    return bernoulli_numbers[N]


print(bernoulliNum(2))