#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    counter = Counter()
    freq = Counter()
    for op, data in queries:
        value = counter[data]
        if op == 1:
            freq[value] = max(freq[value]-1, 0)
            freq[value+1] += 1
            counter[data] = value + 1
        elif op == 3:
            yield 1 if freq[data] else 0
        elif value:
            freq[value] = max(freq[value]-1, 0)
            freq[value-1] += 1
            counter[data] = value - 1
                
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

