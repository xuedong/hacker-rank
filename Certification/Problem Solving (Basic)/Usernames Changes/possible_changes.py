#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    # Write your code here
    n = len(usernames)
    ans = [""] * n
    for i in range(n):
        current = usernames[i]
        l = len(current)
        flag = False
        j = 0
        while j < l-1:
            if current[j+1] < current[j]:
                flag = True
                break
            j += 1
        ans[i] = "YES" if flag else "NO"
    return ans
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

