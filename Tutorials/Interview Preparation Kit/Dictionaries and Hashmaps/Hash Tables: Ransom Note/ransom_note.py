#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1
    for word in note:
        if word in d:
            d[word] -= 1
        else:
            print("No")
            return
    if all([x >= 0 for x in d.values()]):
        print("Yes")
        return
    else:
        print("No")
        return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

