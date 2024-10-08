#Smallest Multiple
#Answer:  232792560
n = 40
l = 0
numList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def isValid (num):
    for i in numList:
        if num%i != 0:
            return False
    return True

while l<100000000:
    # print(n)
    if isValid(n):
        print(n)
        break
    n+=20
    l+=1