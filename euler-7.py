#10001st Prime
#Answer:  104743

def isPrime(num):
    i=2
    while i*i <= num:
        if num%i == 0:
            return False
        i+=1
    return True

def main():
    prime_index = 1
    n = 3
    while prime_index < 10001:
        if isPrime(n):
            prime_index+=1
        n+=1
    return(n-1)