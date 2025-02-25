def fizzbuzz(start, stop):
    output = ""
    for i in range (start, stop + 1):
        output += ( "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or str(i) ) + ", "
    return output[:-2] # remove trailing comma and whitespace
    
print(fizzbuzz(0,100))