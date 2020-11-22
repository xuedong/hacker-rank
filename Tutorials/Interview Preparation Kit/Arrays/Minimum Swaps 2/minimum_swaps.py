#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    arr = [arr[i]-1 for i in range(n)]
    visited = set()
    stack = []
    count = 0
    for i in range(n):
        if arr[i] in visited:
           continue
        else:
            if arr[i] == i:
                visited.add(i)
                continue
            else:
                visited.add(i)
                next = i
                while arr[next] != i:
                    next = arr[next]
                    visited.add(next)
                    count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

