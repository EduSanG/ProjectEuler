#Largest Palindrome Product
#Answer:  906609

import math
product = 0


def check_palindrome(n):
    text = list(str(n))
    for i in range(0, math.floor(len(text)/2)):
        if(text[i] != text[len(text)-i-1]):
            return False
    return True

def main_loop():
    maxPalindrome = 0
    for a in reversed(range(999)):
        for b in reversed(range(999)):
            print(b)
            product = a*b
            if (check_palindrome(product) and product > maxPalindrome):
                maxPalindrome = product
    return maxPalindrome

print(main_loop())