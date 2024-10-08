#Special Pythagorean Triplet
#Answer:  31875000
def findNum():

    a = 997
    b = 2
    c = 1

    while a >= 1:
        while b >= 1:
            print(a,b,c)
            if a*a + b*b == c*c:
                return a*b*c
            b-=1
            c+=1

        a -= 1
        c = 1
        b = 1000-a-c
    return -1

print(findNum())