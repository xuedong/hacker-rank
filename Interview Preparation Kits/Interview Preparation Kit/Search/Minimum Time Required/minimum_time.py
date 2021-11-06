#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    length = len(machines)
    slow = max(machines)
    fast = min(machines)
    upper = math.ceil(goal / length) * slow
    lower = goal // length * fast
    days = (upper + lower) // 2
    products = sum([days//machines[i] for i in range(length)])
    while products != goal:
        if products > goal:
            upper = days
        else:
            lower = days
        if upper - lower <= 1:
            return upper
        days = (upper + lower) // 2
        products = sum([days//machines[i] for i in range(length)])
    while products >= goal:
        days -= 1
        products = sum([days//machines[i] for i in range(length)])
    return days+1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()

