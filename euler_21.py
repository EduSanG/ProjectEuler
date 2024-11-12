
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

def is_amicable(a):
    b = d(get_divisors(a))
    db = d(get_divisors(b))
    return db == a and a != b

def main():
    acc = 0
    for i in range(1, 10000+1):
        if is_amicable(i):
            print(i)
            acc += i
    return acc