
def get_divisors(n):
    count = 2
    i=2
    while n > 1:
        if n%i == 0:
            print(i, ' is a divisor: ', n/i)
            n = n/i
            if n == i:
                count += 1
            else:
                count += 2
        else:
            i+=1
    return count

def get_raw_divisors(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            print(i, ' is a divisor: ', n/i)
            count+=1
    return count

def main():
    return get_divisors(20000000)
    # acc=0
    # for i in range(20):
    #     acc+=i
    #     print(acc)