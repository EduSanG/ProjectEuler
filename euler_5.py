#Smallest Multiple
#Answer:  232792560

numList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def isValid (num):
    for i in numList:
        if num%i != 0:
            return False
    return True

def main():
    n = 40
    l = 0
    while l<100000000:
        if isValid(n):
            return n;
        n+=20
        l+=1