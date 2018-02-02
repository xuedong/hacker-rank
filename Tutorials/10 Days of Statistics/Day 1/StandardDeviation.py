#!/bin/python3

import sys
import math

n = int(input().strip())
arr = [int(arr_i) for arr_i in input().strip().split(' ')]

mean = sum(arr)/n
std = math.sqrt(sum([math.pow((arr_i-mean), 2) for arr_i in arr])/n)

print(std)
