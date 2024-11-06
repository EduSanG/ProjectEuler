#Highly divisible triangular number
#Answer: 76576500
def get_divisors(n):
    div_primes = {}
    i = 2
    while n > 1:
        if (n % i == 0):
            n = n/i
            div_primes[i] = div_primes.get(i, 0) + 1
        else:
            i += 1
    
    acc = 1
    for repeats in div_primes.values():
        acc = acc * (repeats+1)
    
    return acc

def main():
    triangle = 0
    triangle_divisors = 0
    i=1
    while True:
        triangle += i
        triangle_divisors = get_divisors(triangle)
        # print(i, ' ',triangle, '\t', triangle_divisors)
        if triangle_divisors > 500:
            return triangle
        i+=1