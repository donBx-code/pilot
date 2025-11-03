def allPrimesUpTo(num):
    # Your code goes here.
    primesFound = [2]
    divisible = False
    for n in  range(3, num +1):
        print(primesFound)
        divisible = False
        for p in primesFound:
            
            if(n % p ) == 0:
                divisible = True
                break

        if not divisible:
            primesFound.append(n)
    return primesFound

#b = 1000
#a = allPrimesUpTo(b)

#print(a)