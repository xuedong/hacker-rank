#!/bin/python3

import sys

n = int(input().strip())
values = [int(arr_i) for arr_i in input().strip().split(' ')]
freqs = [int(arr_i) for arr_i in input().strip().split(' ')]

arr = []
for i in range(n):
    current = [values[i]] * freqs[i]
    arr.extend(current)
sorted_arr = sorted(arr)

def my_median(arr):
    length = len(arr)
    if length % 2 == 0:
        median = (arr[length//2-1] + arr[length//2])/2
    else:
        median = arr[(length-1)//2]
    return median

def my_quartiles(arr):
    length = len(arr)
    L = arr[0:length//2]
    U = arr[(length+1)//2:]
    q1 = my_median(L)
    q3 = my_median(U)
    return q1, q3

def interquartile(arr):
    q1, q3 = my_quartiles(arr)
    return q3 - q1

print(float(interquartile(sorted_arr)))
