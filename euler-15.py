from time import time

import math

def fact(n): return 1 if n <= 1 else n*fact(n-1)

def bin_coeff(n, k):
    n_fact = fact(n)
    k_fact = fact(k)
    diff_fact = fact(n-k)

    return n_fact / (k_fact * diff_fact)

def number_of_routes(n):
    # The number of routes is the binomial coefficient C(2n, n)
    return bin_coeff(2 * n, n)

def main():
    for i  in range(1, 21):
        start = time()
        print(f'Size: {i}, Result: {number_of_routes(i)}, Time: {time() - start} seconds')
    return 'Done'