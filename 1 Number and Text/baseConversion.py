maxPowerBaseCheck = 16

def convertToBase(num, base):
    output = "-" if sign(num) == -1 else ""
    if (num < 0):
        num *= -1
    for i in range(maxPowerBaseCheck, 0, -1): #backwards index 
        base_value = base**i
        quotient = num // base_value
        if quotient != 0:
            num -= quotient * base_value
            encoded_quotient = encode_number(quotient)
            output = encoded_quotient + output
        else:
            output = "0" + output
    # the "straggling" ones digits
    output = str(num) + output
    # reverse the output
    reversed_output = output[::-1]
    # strip the left zeroes
    reversed_output = reversed_output.lstrip('0')
    return reversed_output

def encode_number(num):
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[num]

def sign(n):
    return (n > 0) - (n < 0)

def convertToBase2(num, base):
    if num == 0:
        return "0"
    
    output = ""
    is_negative = num < 0
    num = abs(num)

    while num > 0:
        quotient = num % base
        output = encode_number(quotient) + output  # Prepend digit
        num //= base  # Move to next place

    if is_negative:
        output = "-" + output  # Handle negatives

    return output

print(convertToBase(33598667, 15))
print(convertToBase2(33598667, 15))