#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.total = None

def build_tree(values, edges):
    nodes = [Node(value, set()) for value in values]
    for u, v in edges:
        nodes[u-1].children.add(nodes[v-1])
        nodes[v-1].children.add(nodes[u-1])
    return nodes[0]

def populate_sum(root):
    stack = (root, None)
    visited = set()

    while stack:
        node = stack[0]
        if node not in visited:
            visited.add(node)
            for child in node.children:
                child.children.remove(node)
                stack = (child, stack)
        else:
             stack = stack[-1]
             node.total = sum(map(lambda child: child.total, node.children)) + node.value

def best_balanced_forest(root):
    stack = (root, None)
    visited, visited_sums, complement_sums = set(), set(), set()
    ans = math.inf

    while stack:
        node = stack[0]
        if node not in visited:
            visited.add(node)
            for child in node.children:
                stack = (child, stack)

            complement_sum = root.total - node.total
            complement_sums.add(complement_sum)

            if ((node.total * 2) in visited_sums or (root.total - node.total * 2) in visited_sums) and node.total * 3 >= root.total:
                current = node.total * 3 - root.total
                if current < ans:
                    ans = current
        else:
            if node.total * 2 == root.total:
                current = node.total
                if current < ans:
                    ans = current

            if (node.total in visited_sums or node.total in complement_sums) and node.total * 3 >= root.total:
                current = node.total * 3 - root.total
                if current < ans:
                    ans = current

            complement_sum = root.total - node.total
            if complement_sum % 2 == 0:
                half = complement_sum // 2
                if half > node.total and (half in visited_sums or half in complement_sums):
                    current = half - node.total
                    if current < ans:
                        ans = current

            complement_sums.remove(complement_sum)
            visited_sums.add(node.total)

            stack = stack[-1]

    if ans == math.inf:
        return -1
    return ans

def balancedForest(values, edges):
    root = build_tree(values, edges)
    populate_sum(root)
    return best_balanced_forest(root)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()

