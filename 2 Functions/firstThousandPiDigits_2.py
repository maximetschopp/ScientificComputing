from fractions import Fraction
from tqdm import tqdm # progress bar

def arctan(x):
    x = Fraction(x) # in case x isnt a fraction, obv it is but if i make a dumb dumb
    T_k = x
    k = 1
    arctan_sum = T_k
    last_term = Fraction(1, 1)

    while abs(last_term) > Fraction(1, 10**1000):
        T_k = -x**2 * T_k  # T_k = -x^2 * T_{k-1}
        last_term = T_k / (2 * k + 1)
        k+=1
        arctan_sum += last_term
    
    return arctan_sum

arctan_1_2 = arctan(Fraction(1, 2))
arctan_1_3 = arctan(Fraction(1, 3))

pi_approx = 4 * (arctan_1_2 + arctan_1_3)

a = int(pi_approx)
b = int((pi_approx - a) * 10**1000)
pi_decimal = str(a) + "." + str(b)


# Get the first 1000 decimal places
pi_str = pi_decimal[:1002]  # 1000 + 2 bc we need 1000 digits after decimal point

print("-" * 140)
print(pi_str)
print("-" * 140)
print(pi_str[947:961])