#!usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    res = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            rep = chr((ord(char) + k - 65) % 26 + 65)
            res += rep
            continue
        if char.islower():
            rep = chr((ord(char) + k - 97) % 26 + 97)
            res += rep
            continue
        res += char
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

