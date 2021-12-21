#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

P=10**9+7


def solve(n, m):
    # Write your code here
    numerator = math.factorial(n+m-1) % P
    denominator = math.factorial(n) * math.factorial(m-1)
    denominator = pow(denominator, P-2, P)
    return (denominator * numerator) % P


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

