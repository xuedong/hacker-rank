#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    # solve here
    n = len(arr)
    for query in queries:
        best = max([query^arr[i] for i in range(n)])
        print(best)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

