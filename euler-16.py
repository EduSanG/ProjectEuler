

def main():
    n = 2**1000
    digit_arr = list(str(n))
    acc = 0
    for digit_string in digit_arr:
        acc += int(digit_string)
    return acc