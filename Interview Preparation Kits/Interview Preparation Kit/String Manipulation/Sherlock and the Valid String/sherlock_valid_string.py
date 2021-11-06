#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if len(s) == 0:
        return "YES"
    
    freqs = {}
    smallest = s[0]
    biggest = s[0]
    for i in range(len(s)):
        if s[i] in freqs:
            freqs[s[i]] += 1
        else:
            freqs[s[i]] = 1
        if freqs[s[i]] < freqs[smallest]:
            smallest = s[i]
        if freqs[s[i]] > freqs[biggest]:
            biggest = s[i]
    
    new_small = {k: v for k, v in freqs.items() if v > freqs[smallest]}
    new_big = {k: v for k, v in freqs.items() if v < freqs[biggest]}
    if len(new_small) >= 2 and len(new_big) >= 2:
        return "NO"
    elif len(new_small) == 1 and list(new_small.values())[0] >= freqs[smallest] + 2:
        return "NO"
    elif len(new_big) == 1 and list(new_big.values())[0] > 1:
        return "NO" 
    else:
        return "YES"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

