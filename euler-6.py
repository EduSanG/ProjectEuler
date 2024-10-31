#Sum Square Difference
#Answer:  25164150
def main():
    a = 0
    b = 0
    for n in range(1, 101):
        a+=(n*n)
        b+=n
    b=b*b
    return b-a