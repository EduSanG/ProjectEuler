
def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def div_sum(nums):
    acc = 0
    for num in nums:
        acc += num
    return acc

def is_abundant(n):
    divisors = get_divisors(n)
    return div_sum(divisors) > n

def can_be_summed(n, nums):
    abundants = list(filter(lambda x: x < n , nums))
    for i in range(0, len(abundants)-1):
        for j in range(0, len(abundants)):
            if n == (abundants[i] + abundants[j]):
                return True
    return False

def main():
    num_range = range(1, 28123)

    abundants = list(filter(lambda x: is_abundant(x) ,[i for i in reversed(num_range)]))
    print(abundants)

    acc=0
    for num in num_range:
        print('Checking: ', num)
        if not can_be_summed(num, abundants):
            acc += num
    return acc