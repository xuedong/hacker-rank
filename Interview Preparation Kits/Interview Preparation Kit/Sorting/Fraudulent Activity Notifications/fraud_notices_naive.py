#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def counting_sort(arr):
    size = len(arr)
    output = [0] * size

    # Initialize the counting array
    count = [0] * 201
    for i in range(size):
        count[arr[i]] += 1

    # Update the cumulative counts
    for i in range(1, 201):
        count[i] += count[i-1]

    # Place each element in the correct index
    for i in range(size):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n//2]
    else:
        return (arr[n//2]+arr[n//2-1])/2

def activityNotifications(expenditure, d):
    notices = 0

    n = len(expenditure)
    if n <= d:
        return 0

    for i in range(d, n):
        sorted_trans = counting_sort(expenditure[i-d:i])
        med = median(sorted_trans)
        if expenditure[i] >= 2 * med:
            notices += 1
    
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

