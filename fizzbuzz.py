def fizzbuzzOld(start, stop):
    output = ""
    for i in range (start, stop +1):
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        elif i % 3 != 0:
            output += str(i)
        output += ", "
    return output
    
def fizzbuzz(start, stop):
    output = ""
    for i in range (start, stop + 1):
        output += ( "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or str(i) ) + ", "
    return output[:-2] # remove trailing comma and whitespace
    
print(fizzbuzz(0,100))