#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    arr.sort()
    res, i = 0, 0
    while i < len(arr)-1:
        if arr[i+1] - arr[i] == k:
            res += 1
            i += 1
        elif arr[i+1] - arr[i] > k:
            i += 1
        else:
            j = i+1
            while j <= len(arr)-1 and arr[j] - arr[i] < k:
                j += 1
            if j <= len(arr)-1 and arr[j] - arr[i] == k:
                res += 1
            i += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

