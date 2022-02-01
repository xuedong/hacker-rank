#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
 
    for i in range(len(s)//2+1):
        if s[i] == s[len(s)-i-1]:
            continue
        new_string_start = s[:i] + s[i+1:]
        if new_string_start == new_string_start[::-1]:
            return i
        new_string_end = s[:len(s)-i-1] + s[len(s)-i:]
        if new_string_end == new_string_end[::-1]:
            return len(s)-i-1

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

