#!/bin/python3

import sys
import math

_m = int(pow(10, 9))+7

def towerColoring(n):
    # Complete this function
    global _m
    
    if n == 0:
        return 3
    elif n == 1:
        return 27
    elif n == 2:
        return 3**9
    else:
        aux = towerColoring(n-3)
        res = pow(aux, 27, _m)

    return res

n = int(input().strip())
result = towerColoring(n)
print(result)
