#Summation of Primes
#Answer: 142913828922
from functools import reduce


def isPrime(num):
    i=2
    while i*i <= num:
        if num%i == 0:
            return False
        i+=1
    return True

def main():
    l = []
    for n in range(2, 2000000):
        if isPrime(n):
            l.append(n)

    answer = reduce(lambda a,b: a+b,l)
    return answer
