

def fact(n):
    if n == 1: return 1
    return n*fact(n-1)

def main():
    big_n = fact(100)
    acc = 0
    for n in list(str(big_n)):
        acc += int(n)
    return acc