#!/bin/python3

import os
import sys
sys.setrecursionlimit(1500)

from queue import Queue

#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self, index, depth):
        self.index = index
        self.depth = depth
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.index)

def print_in_order(node, result):
    if node.left:
        print_in_order(node.left, result)
    result.append(node.index)
    if node.right:
        print_in_order(node.right, result)

def swap_in_order(node, ks):
    if node.left:
        swap_in_order(node.left, ks)
    if node.right:
        swap_in_order(node.right, ks)

    if node.depth in ks:
        node.left, node.right = node.right, node.left

    return node

def create_tree(indexes):
    q = Queue()
    root = Node(1, 1)
    depth = 1

    q.put(root)
    for left, right in indexes:
        current = q.get()
        if left != -1:
            left_node = Node(left, current.depth+1)
            current.left = left_node
            q.put(left_node)
        if right != -1:
            right_node = Node(right, current.depth+1)
            current.right = right_node
            q.put(right_node)
        depth = current.depth

    return root, depth

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #   
    num_queries = len(queries)
    results = []

    tree, depth = create_tree(indexes)
    for k in queries:
        ks = [x for x in range(1, depth+1) if x % k == 0]
        root = swap_in_order(tree, ks)
        result = []
        print_in_order(root, result)
        results.append(result)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

