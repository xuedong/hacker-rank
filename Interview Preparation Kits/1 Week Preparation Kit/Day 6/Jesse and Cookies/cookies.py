#!/usr/bin/env python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    n = len(A)
    if n == 1:
        return 0 if A[0] >= k else -1

    A.sort()

    i = 0
    while len(A) >= 2 and A[0] < k:
        element = A[0] + 2 * A[1]
        A.pop(0)
        A.pop(0)
        bisect.insort(A, element)
        i += 1

    return i if A[0] >= k else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()

