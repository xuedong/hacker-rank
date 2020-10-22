#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    num_a = s.count("a", 0, length)
    rest = n % length
    rest_a = s.count("a", 0, rest)
    return (n // length) * num_a + rest_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

