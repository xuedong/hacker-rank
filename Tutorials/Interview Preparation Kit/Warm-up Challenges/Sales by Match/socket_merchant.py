#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if n <= 1:
        return 0
    else:
        pairs = 0
        i = 0
        while i < len(ar) and len(ar) > 0:
            j = i+1
            flag = True
            while j < len(ar):
                if ar[j] == ar[i]:
                    pairs += 1
                    ar.pop(j)
                    ar.pop(i)
                    flag = False
                    break
                j += 1
            if flag:
                i += 1
        return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

