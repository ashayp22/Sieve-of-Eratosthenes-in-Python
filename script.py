import numpy as np

def SieveOfEratosthenes(max):
    crossed = [] #starts at 0, ends with max(inclusive)
    for i in range(max+1):
        crossed.append(False)
    crossed[0] = True
    crossed[1] = True

    #now starts crossing out
    current_num = 2 #starting number

    while current_num**2 <= max:
        if not crossed[current_num]: #not yet crossed, can be a multiple
            for j in range(current_num*2, max+1, current_num): #every multiple of current num up till the max
                crossed[j] = True #is crossed now
        current_num += 1 #increases the current number

    #now gets list of primes
    primes = []
    for i in range(len(crossed)):
        if not crossed[i]:
            primes.append(i)
    primes = np.array(primes)
    return primes

p = SieveOfEratosthenes(10000)
print("number of primes: " + str(len(p)))
print("biggest prime: " + str(np.amax(p)))
print("all primes: ")
print(p)
