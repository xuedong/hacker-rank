#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    n = len(arr)
    arr = sorted(arr)

    fairness = arr[n-1] - arr[0]
    for i in range(n-k+1):
        current = arr[i+k-1] - arr[i]
        fairness = min(current, fairness)

    return fairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

