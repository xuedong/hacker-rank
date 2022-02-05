#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for i in range(len(s)):
        ch = s[i]

        if ch == "{" or ch == "(" or ch == "[":
            stack.append(ch)
        else:
            if not stack:
                return "NO"

            if stack[-1] == "{" and ch == "}":
                stack.pop()
            elif stack[-1] == "(" and ch == ")":
                stack.pop()
            elif stack[-1] == "[" and ch == "]":
                stack.pop()
            else:
                return "NO"

    if len(stack) > 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

