#!/bin/python3
import sys


def geo_dist(n, p, q):
    return p * q**(n-1)

arr = [int(arr_i) for arr_i in input().strip().split(' ')]
n = int(input())
a = arr[0]
b = arr[1]

p = a / b
q = 1 - p

print(round(geo_dist(n, p, q), 3))

