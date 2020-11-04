#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    current = b
    for letter in a:
        if letter in current:
            count += 1
            current = current.replace(letter, '', 1)
    return len(a) + len(b) - 2 * count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

