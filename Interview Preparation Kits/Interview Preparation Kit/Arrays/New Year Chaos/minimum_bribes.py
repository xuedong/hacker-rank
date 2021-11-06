#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    count = 0
    for i in range(n):
        if q[i] >= i+4:
            print("Too chaotic")
            return
        else:
            for j in range(max(q[i]-2, 0), i):
                if q[j] > q[i]:
                    count += 1
    print(str(count))
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

