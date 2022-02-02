#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def digit_sum(n):
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    return res


def super_digit_1(n):
    if len(n) == 1:
        return int(n)
    return super_digit_1(str(digit_sum(n)))


def superDigit(n, k):
    # Write your code here
    if k == 1:
        return super_digit_1(n)
    else:
        return super_digit_1(str(digit_sum(n)*k))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

