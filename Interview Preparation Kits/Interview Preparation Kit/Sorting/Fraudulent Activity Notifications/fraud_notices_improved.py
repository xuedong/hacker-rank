#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def get_twice_median(arr, d, count):
    cumulative = count.copy()
    for i in range(1, 201):
        cumulative[i] += cumulative[i-1]

    if d % 2 == 0:
        i = 0
        while i < 201:
            if d // 2 <= cumulative[i]:
                low = i
                break
            i += 1
        while i < 201:
            if d // 2 + 1 <= cumulative[i]:
                high = i
                break
            i += 1
        return low + high
    else:
        i = 0
        while i < 201:
            if d // 2 + 1 <= cumulative[i]:
                median = i
                return 2 * median
            i += 1

def activityNotifications(expenditure, d):
    notices = 0

    n = len(expenditure)
    if n <= d:
        return 0

    count = [0] * 201
    for i in range(d):
        count[expenditure[i]] += 1

    for i in range(d, n):
        twice_median = get_twice_median(expenditure, d, count)
        if expenditure[i] >= twice_median:
            notices += 1
        count[expenditure[i]] += 1
        count[expenditure[i-d]] -= 1
    
    return notices


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

