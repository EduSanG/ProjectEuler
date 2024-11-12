

def collatz_count(n):
    i=1
    while n > 1:
        n = n/2 if n%2==0 else 3*n+1
        i+=1
    return i

def main():
    max_collatz = 0
    max_collatz_count = 0
    buff = 0
    for i in range (1,1000000):
        buff = collatz_count(i)
        if buff > max_collatz_count:
            max_collatz_count = buff
            max_collatz = i
    return max_collatz  