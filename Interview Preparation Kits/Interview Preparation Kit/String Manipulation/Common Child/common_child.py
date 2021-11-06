#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    if s1[0] == s2[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    for k in range(1, n):
        if dp[k-1][0] == 1:
            dp[k][0] = 1
        elif dp[k-1][0] == 0 and s2[0] == s1[k]:
            dp[k][0] = 1
        else:
            dp[k][0] = 0
        if dp[0][k-1] == 1:
            dp[0][k] = 1
        elif dp[0][k-1] == 0 and s1[0] == s2[k]:
            dp[0][k] = 1
        else:
            dp[0][k] = 0
            
    for i in range(1, n):
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    return dp[n-1][n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

