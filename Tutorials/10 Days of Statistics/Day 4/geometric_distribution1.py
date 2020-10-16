# Enter your code here 
#!/bin/python3
import sys
from math import factorial as fac


def binomial(x, y):
    try:
        return fac(x) // fac(y) // fac(x-y)
    except ValueError:
        return 0

def neg_bin_dist(n, k, p, q):
    return binomial(n-1, k-1) * p**k * q**(n-k)

arr = [int(arr_i) for arr_i in input().strip().split(' ')]
n = int(input())
a = arr[0]
b = arr[1]

p = a / b
q = 1 - p

print(round(neg_bin_dist(n, 1, p, q), 3))

