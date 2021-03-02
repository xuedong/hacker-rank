#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the decibinaryNumbers function below.
# def db_to_dec(x):
#     ans = 0
#     power = 1
#     while x:
#         rest = x % 10
#         ans += power * rest
#         power *= 2
#         x = x//10
#     return ans

MAX = 300000
DIGITS = 10
POWERS = 20

count = [[0 for _ in range(POWERS)] for _ in range(MAX)]
count_below = [0 for _ in range(MAX)]

def pre_compute():
    for n in range(MAX):
        count[n][0] = 1 if n < DIGITS else 0
        for j in range(1, POWERS):
            for d in range(DIGITS):
                value = n - d * (1 << j)
                if value < 0:
                    break
                count[n][j] += count[value][j-1]

    for n in range(1, MAX):
        count_below[n] = count_below[n-1] + count[n-1][POWERS-1]

def decibinaryNumbers(x):
    result = 0
    l = bisect.bisect_left(count_below, x) - 1
    value = l - count_below[0]
    offset = x - 1 - count_below[l]

    for i in reversed(range(1, POWERS)):
        power = 1 << i
        for digit in range(DIGITS):
            current = value - digit * power
            if offset < count[current][i-1]:
                result += digit
                value -= digit * power
                break
            offset -= count[current][i-1]
        result *= 10

    result += value
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    pre_compute()

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()

