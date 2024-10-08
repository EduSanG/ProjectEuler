#Summation of Primes
#Answer: 142913828922
from functools import reduce


l = []
def isPrime(num):
    i=2
    while i*i <= num:
        if num%i == 0:
            return False
        i+=1
    return True

for n in range(2, 2000000):
    print(n)
    if isPrime(n):
        l.append(n)

answer = reduce(lambda a,b: a+b,l)

print(answer)