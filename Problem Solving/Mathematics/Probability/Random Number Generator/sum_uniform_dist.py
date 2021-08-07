#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def solve(a, b, c):
    # Write your code here
    if a + b <= c:
        return 1, 1

    if c <= a and c <= b:
        x = c * c
        y = 2 * a * b
        d = gcd(x, y)
        return x//d, y//d

    if c >= a and c >= b:
        x = 2 * a * b - (b - c + a) ** 2
        y = 2 * a * b
        d = gcd(x, y)
        return x//d, y//d

    a, b = max(a, b), min(a, b)
    x = c * c - (c - b) ** 2
    y = 2 * a * b
    d = gcd(x, y)
    return x//d, y//d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        x, y = solve(a, b, c)

        fptr.write("{}/{}".format(x, y) + '\n')

    fptr.close()

