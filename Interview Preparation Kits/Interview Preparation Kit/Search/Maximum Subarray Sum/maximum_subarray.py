#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def maximumSum(a, m):
    n = len(a)
    prefix = [0] * n
    current = 0
    for i in range(n):
        current = (a[i] % m + current) % m
        prefix[i] = current
        
    sorted_prefix = sorted(prefix)
    sorted_index = sorted(range(n), key=lambda k: prefix[k])
    smallest = m
    for i in range(n-1):
        if sorted_index[i] > sorted_index[i+1]:
            diff = sorted_prefix[i+1] - sorted_prefix[i]
            if diff < smallest:
                smallest = diff
    
    return max(m-smallest, sorted_prefix[n-1])
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

