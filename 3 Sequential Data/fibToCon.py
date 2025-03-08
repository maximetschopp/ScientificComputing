def conways (N):
    output = [5,4]
    for i in range (2, N):
        fibNum = output[i-2] + output[i-1]
        check = False
        for k in range(2, int(fibNum ** 0.5) + 1):
            if fibNum % k == 0:
               output.append(fibNum // k)
               check = True
               break
        
        if not check: 
            output.append(fibNum)

    return output

print(conways(26))