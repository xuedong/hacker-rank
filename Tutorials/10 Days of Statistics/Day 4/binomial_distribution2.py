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

def f(n, k, p, q):
    mass = 0
    for i in range(k+1):
        mass += bin_dist(n, i, p, q)
    return mass

def g(n, k, p, q):
    mass = 0
    for i in range(k, n+1):
        mass += bin_dist(n, i, p, q)
    return mass

arr = [int(arr_i) for arr_i in input().strip().split(' ')]
a = arr[0]
n = arr[1]

p = a / 100
q = 1 - p

print(round(f(n, 2, p, q), 3))
print(round(g(n, 2, p, q), 3))

