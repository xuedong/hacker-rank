#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        max_sum1 = max(arr[0], arr[1])
        max_sum2 = arr[0]
        max_sum = max(arr[0], arr[1])
        for i in range(2, n):
            max_sum = max(arr[i], max(max_sum2+arr[i], max_sum1))
            max_sum2 = max_sum1
            max_sum1 = max_sum
        return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

