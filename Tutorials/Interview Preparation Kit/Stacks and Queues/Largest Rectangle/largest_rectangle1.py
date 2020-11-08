#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def compute(h, i):
    n = len(h)
    if n == 1:
        return h[0]
    p1 = i + 1
    p2 = i - 1
    total = h[i]
    while p1 < n:
        if h[p1] >= h[i]:
            total += h[i]
            p1 += 1
        else:
            break
    while p2 >= 0:
        if h[p2] >= h[i]:
            total += h[i]
            p2 -= 1
        else:
            break
    return total

def largestRectangle(h):
    best = 0
    for i in range(len(h)):
        current = compute(h, i)
        print(current)
        if current > best:
            best = current
    return best


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

