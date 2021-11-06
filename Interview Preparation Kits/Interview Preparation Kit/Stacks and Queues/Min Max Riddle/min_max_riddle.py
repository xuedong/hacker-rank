#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the riddle function below.
def create_dict(arr):
    len_dict = defaultdict(int)
    stack = []

    i = 0
    while i < len(arr):
        if not stack or arr[stack[-1]] <= arr[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            len_dict[arr[top]] = max(len_dict[arr[top]], i-stack[-1]-1 if stack else i)

    while stack:
        top = stack.pop()
        len_dict[arr[top]] = max(len_dict[arr[top]], i-stack[-1]-1 if stack else i)

    return len_dict

def riddle(arr):
    # complete this function
    n = len(arr)
    len_dict = create_dict(arr)

    inv_dict = defaultdict(int)
    for key in len_dict:
        inv_dict[len_dict[key]] = max(inv_dict[len_dict[key]], key)

    ans = [inv_dict[n]]
    for i in reversed(range(1, n)):
        if inv_dict[i] < ans[-1]:
            ans.append(ans[-1])
        else:
            ans.append(inv_dict[i])

    return reversed(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

