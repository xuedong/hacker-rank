#!/bin/python3

import sys
import numpy as np

from collections import Counter

n = int(input().strip())
arr = [int(arr_i) for arr_i in input().strip().split(' ')]

mean = np.sum(arr)/n
print(round(mean, 1))

sorted_arr = sorted(arr)
if n % 2 == 0:
    median = (sorted_arr[n//2-1] + sorted_arr[n//2])/2
else:
    median = sorted_arr[(n-1)//2]
print(round(median, 1))

mode = max(sorted_arr, key=sorted_arr.count)
print(mode)
