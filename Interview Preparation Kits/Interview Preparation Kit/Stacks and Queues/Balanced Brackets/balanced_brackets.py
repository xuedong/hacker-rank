#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            stack.append(s[i])
        elif len(stack) == 0:
                return 'NO'     
        elif s[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 'NO'
        elif s[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'NO'
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
            
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

