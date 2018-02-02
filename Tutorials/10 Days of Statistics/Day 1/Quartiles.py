#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_i) for arr_i in input().strip().split(' ')]

def my_median(arr):
    length = len(arr)
    if length % 2 == 0:
        median = (arr[length//2-1] + arr[length//2])/2
    else:
        median = arr[(length-1)//2]
    return median

X = sorted(arr)
L = X[0:n//2]
U = X[(n+1)//2:]

print(int(my_median(L)))
print(int(my_median(X)))
print(int(my_median(U)))
