#!/bin/python3
import sys
from math import factorial as fac


def binomial(x, y):
    try:
        return fac(x) // fac(y) // fac(x - y)
    except ValueError:
        return 0

def bin_dist(n, k, p, q):
    return binomial(n, k) * p**k * q**(n-k)

def f(p, q):
    p1 = bin_dist(6, 0, p, q)
    p2 = bin_dist(6, 1, p, q)
    p3 = bin_dist(6, 2, p, q)
    return 1 - p1 - p2 - p3

arr = [float(arr_i) for arr_i in input().strip().split(' ')]
a = arr[0]
b = arr[1]

p = a/(a+b)
q = b/(a+b)

print(round(f(p, q), 3))

