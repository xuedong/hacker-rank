#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    arr = [0] * (n1+n2)
    i, j = 0, 0
    k = 0
    
    count = 0
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            j += 1
            k += 1
            count += n1-i
    
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1
    
    return arr, count

def sort(arr):
    n = len(arr)
    if n == 1:
        return arr, 0

    mid = n // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    
    arr1, count1 = sort(arr1)
    arr2, count2 = sort(arr2)
    arr, count = merge(arr1, arr2)
    
    return arr, count+count1+count2
    
def countInversions(arr):
    arr, count = sort(arr)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

