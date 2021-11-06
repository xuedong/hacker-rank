#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n = len(c)
    c = sorted(c)
    cost = 0
    counts = [0] * k
    current = 0

    for i in reversed(range(n)):
        cost += (counts[current] + 1) * c[i]
        counts[current] += 1
        current += 1
        if current == k:
            current = 0

    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

