#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos, neu, neg = 0, 0, 0
    for i in range(n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] == 0:
            neu += 1
        else:
            neg += 1
    print('{:.6f}'.format(pos/n))
    print('{:.6f}'.format(neg/n))
    print('{:.6f}'.format(neu/n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

