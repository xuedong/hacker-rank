#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = []
    n = len(p)
    ans = 0
    for i in range(n):
        count = 0
        while stack and p[i] <= stack[-1][0]:
            count = max(count, stack.pop()[1])
        if stack:
            count += 1
        else:
            count = 0
        ans = max(count, ans)
        stack.append((p[i], count))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

