#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
class Node():
    def __init__(self):
        self.left = None
        self.right = None

def insert(x, head):
    current = head

    for i in reversed(range(31)):
        value = (x >> i) & 1
        if value == 0:
            if not current.left:
                current.left = Node()
            current = current.left
        else:
            if not current.right:
                current.right = Node()
            current = current.right

def maxXor(arr, queries):
    # solve here
    n = len(arr)
    m = len(queries)
    head = Node()
    for i in range(n):
        insert(arr[i], head)

    for i in range(m):
        xor = 0
        power = pow(2, 30)
        node = head
        for j in reversed(range(31)):
            value = (queries[i] >> j) & 1
            if value == 0:
                if node.right:
                    xor += power
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:
                    xor += power
                    node = node.left
                else:
                    node = node.right
            power //= 2

        print(xor)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

