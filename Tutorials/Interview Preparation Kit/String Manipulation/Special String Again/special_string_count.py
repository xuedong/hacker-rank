#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    counts = []
    current = None
    count = 0
    ans = 0
    
    for i in range(n):
        if s[i] == current:
            count += 1
        else:
            if current is not None:
                counts.append((current, count))
            current = s[i]
            count = 1
    counts.append((current, count))

    length = len(counts)
    for j in range(length):
        ans += (counts[j][1] + 1) * counts[j][1] // 2
        
    for k in range(1, length-1):
        if counts[k-1][0] == counts[k+1][0] and counts[k][1] == 1:
            ans += min(counts[k-1][1], counts[k+1][1])
    
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

