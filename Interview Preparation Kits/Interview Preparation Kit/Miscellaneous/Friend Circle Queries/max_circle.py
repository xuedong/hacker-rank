#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def find(x, parent):
    while parent[x] != x:
        x = parent[x]
    return x

def maxCircle(queries):
    parent = {}
    size = {}
    best = 0
    ans = []

    for query in queries:
        x, y = query
        if x not in parent:
            parent[x] = x
        if y not in parent:
            parent[y] = y
        if x not in size:
            size[x] = 1
        if y not in size:
            size[y] = 1

        parent_x = find(x, parent)
        parent_y = find(y, parent)
        if parent_x != parent_y:
            if size[parent_x] > size[parent_y]:
                parent[parent_y] = parent_x
                size[parent_x] = size[parent_x] + size[parent_y]
            else:
                parent[parent_x] = parent_y
                size[parent_y] = size[parent_x] + size[parent_y]
            best = max(best, max(size[parent_x], size[parent_y]))

        ans.append(best)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

