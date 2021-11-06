#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    counts = defaultdict(int)
    occurences = defaultdict(int)
    for ch in s:
        counts[ch] += 1
        occurences[ch] += 1

    visits = defaultdict(int)
 
    ans = []
    n = len(s)
    for i in reversed(range(n)):
        ch = s[i]
        if occurences[ch] // 2 - visits[ch] > 0:
            while ans and ans[-1] > ch and visits[ans[-1]] + counts[ans[-1]] - 1 >= occurences[ans[-1]] // 2:
                rm = ans.pop()
                visits[rm] -= 1
            visits[ch] += 1
            ans.append(ch)
        counts[ch] -= 1
 
    return "".join(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

