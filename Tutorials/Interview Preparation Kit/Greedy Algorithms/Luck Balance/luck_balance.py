#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    importants = []
    unimportants = []
    for i in range(len(contests)):
        if contests[i][1] == 1:
            importants.append(contests[i][0])
        else:
            unimportants.append(contests[i][0])
    importants.sort()
    n = len(importants)
    total = sum(unimportants)
    if k >= n:
        total += sum(importants)
    else:
        total += sum(importants[n-k:]) - sum(importants[0:n-k])
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

