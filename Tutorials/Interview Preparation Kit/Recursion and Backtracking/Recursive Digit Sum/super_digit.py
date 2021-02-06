#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    def aux(n):
        if n // 10 == 0:
            return n
        else:
            n = sum([int(str(n)[i]) for i in range(len(str(n)))])
            return aux(n)
    number = sum([int(str(n)[i]) for i in range(len(str(n)))]) * k
    return aux(int(number))
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

