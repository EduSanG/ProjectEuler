#Summation of Primes
#Answer: 142913828922

target = 2000000
primes = [True for n in range(target+1)]

def sieve(n):
    for i in range(n*n, target+1, n):
        primes[i] = False


def main():
    answer = 0
    i=2
    while i < target:
        if primes[i]:
            answer += i
            sieve(i)
        i+=1
    return answer