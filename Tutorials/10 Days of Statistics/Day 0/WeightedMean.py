#!/bin/python3

import sys

n = int(input().strip())
values = [int(arr_i) for arr_i in input().strip().split(' ')]
weights = [int(arr_i) for arr_i in input().strip().split(' ')]


weighted_mean = sum([values[i]*weights[i] for i in range(n)]) / sum(weights)
print(round(weighted_mean, 1))
