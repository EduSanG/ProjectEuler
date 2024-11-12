
def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def d(divs):
    acc = 0
    for i in divs:
        acc += i
    return acc

def is_amicable(n):
    dn = d(get_divisors(n))
    return d(get_divisors(dn)) == n

def main():
    acc = 0
    for i in range(1, 10000+1):
        if is_amicable(i):
            print(i)
            acc += i
    return acc