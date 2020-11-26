#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    count = {}
    ans = [0] * len(list(filter(lambda x: x == 3, [queries[i][0] for i in range(len(queries))])))
    index = 0
    for i in range(len(queries)):
        if queries[i][0] == 1:
            j = queries[i][1]
            count[j] = count.get(j, 0) + 1
        elif queries[i][0] == 2:
            j = queries[i][1]
            if j in count:
                count[j] -= 1
                if count[j] == 0:
                    del count[j]
        else:
            j = queries[i][1]
            if j in count.values():
                ans[index] = 1
            index += 1
    return ans
                
 
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

