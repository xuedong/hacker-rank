#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.       
def triplets(a, b, c):
    sorted_a = list(sorted(set(a)))
    sorted_b = list(sorted(set(b)))
    sorted_c = list(sorted(set(c)))
    total = 0
    ai = 0
    bi = 0
    ci = 0
    while bi < len(sorted_b):
        while ai < len(sorted_a) and sorted_a[ai] <= sorted_b[bi]:
            ai += 1
        while ci < len(sorted_c) and sorted_c[ci] <= sorted_b[bi]:
            ci += 1
        total += ai * ci
        bi += 1
    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

