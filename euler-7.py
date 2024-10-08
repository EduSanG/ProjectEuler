#10001st Prime
#Answer:  104743

import math

prime_index = 1
n = 3

def isPrime(num):
    i=2
    while i*i <= num:
        if num%i == 0:
            return False
        i+=1
    return True

while prime_index < 10001:
    if isPrime(n):
        prime_index+=1
        print(n, prime_index)
    n+=1