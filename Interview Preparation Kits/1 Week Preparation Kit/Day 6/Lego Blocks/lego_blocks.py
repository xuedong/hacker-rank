#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    MOD = 1000000007

    layouts_1 = [0, 1, 2, 4, 8]
    for i in range(5, m+1):
        layouts_1.append((layouts_1[i-1] + layouts_1[i-2] + layouts_1[i-3] + layouts_1[i-4]) % MOD)

    layouts_total = [0] * (m+1)
    for i in range(1, m+1):
        layouts_total[i] = pow(layouts_1[i], n, MOD)

    layouts_good = [layouts_total[i] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, i):
            layouts_good[i] -= layouts_good[j] * layouts_total[i-j]
        layouts_good[i] = layouts_good[i] % MOD

    return layouts_good[m]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

