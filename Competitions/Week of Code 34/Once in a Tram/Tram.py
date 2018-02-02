#!/bin/python3

import sys

def isLucky(n):
    myStr = str(n)
    arr = [int(arr_i) for arr_i in list(myStr)]

    return (arr[0] + arr[1] + arr[2] == arr[3] + arr[4] + arr[5])

def onceInATram(x):
    i = x+1
    while not isLucky(i):
        i += 1
    return i

if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x)
    print(result)
