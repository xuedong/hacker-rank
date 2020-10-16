#!/bin/python3
import sys


arr = [float(arr_i) for arr_i in input().strip().split(' ')]
mean1 = arr[0]
mean2 = arr[1]

print(round(160+40*(mean1+mean1**2), 3))
print(round(128+40*(mean2+mean2**2), 3))

