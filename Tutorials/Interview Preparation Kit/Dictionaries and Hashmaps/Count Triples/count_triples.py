#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    dict_single = {}
    dict_pair = {}
    count = 0
    for e in reversed(arr):
        if e * r in dict_pair:
            count += dict_pair[e*r]
        if e * r in dict_single:
            dict_pair[e] = dict_pair.get(e, 0) + dict_single[e*r]
        
        dict_single[e] = 1 + dict_single.get(e, 0)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

