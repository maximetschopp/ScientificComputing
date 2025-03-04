from fractions import Fraction
from decimal import Decimal, getcontext
from tqdm import tqdm # progress bar


# Set precision to 1005 to ensure accuracy for 1000 digits
getcontext().prec = 1005

def arctan(x, terms=5000):
    x = Fraction(x) # in case x isnt a fraction, obv it is but if i make a dumb dumb
    T_k = x
    arctan_sum = T_k

    for k in tqdm(range(1, terms), desc=("Arctan " + str(float(x)))):
        T_k = -x**2 * T_k  # T_k = -x^2 * T_{k-1}
        arctan_sum += T_k / (2 * k + 1)
    
    return arctan_sum

arctan_1_2 = arctan(Fraction(1, 2))
arctan_1_3 = arctan(Fraction(1, 3))

pi_approx = 4 * (arctan_1_2 + arctan_1_3)

# Use the Decimal class which has built in precision 
pi_decimal = Decimal(pi_approx.numerator) / Decimal(pi_approx.denominator)

# Get the first 1000 decimal places
pi_str = str(pi_decimal)[:1002]  # 1000 + 2 bc we need 1000 digits after decimal point

print("-" * 140)
print(pi_str)
print("-" * 140)
print(pi_str[947:961])
