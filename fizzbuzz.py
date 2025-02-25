def fizzbuzz(start, stop):
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
    
    
print(fizzbuzz(0,100))