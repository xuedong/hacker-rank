#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    new_dict = defaultdict(list)
    for i in range(len(cost)):
        new_dict[cost[i]].append(i+1)
    for c in new_dict:
        if (money-c) != c and (money-c) in new_dict:
            if new_dict[c][0] < new_dict[money-c][0]:
                print(str(new_dict[c][0])+' '+str(new_dict[money-c][0]))
            else:
                print(str(new_dict[money-c][0])+' '+str(new_dict[c][0]))
            return
        elif (money-c) == c:
            if len(new_dict[c]) > 1:
                print(str(new_dict[c][0])+' '+str(new_dict[c][1]))
                return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

