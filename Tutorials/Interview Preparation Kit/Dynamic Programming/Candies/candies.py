#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    if n == 1:
        return 1
    
    dp = [1 for i in range(n)]
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
                 
    for i in reversed(range(0, n-1)):
        if arr[i] > arr[i+1]:
            dp[i] = max(dp[i+1] + 1, dp[i])
            
    return sum(dp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

