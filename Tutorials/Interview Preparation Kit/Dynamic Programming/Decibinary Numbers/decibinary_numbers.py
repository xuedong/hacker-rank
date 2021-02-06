#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decibinaryNumbers function below.
def db_to_dec(x):
    ans = 0
    power = 0
    while x:
        rest = x % 10
        ans += 2**power*rest
        power *= 2
        x = x//10
    return ans
 
def decibinaryNumbers(x):
    pass

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x)
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()

