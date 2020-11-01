#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.
from collections import defaultdict
#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def bfs(graph, ids, visited, target, start):
    visited.add(start)
    ans = 0
    if start in graph:
        finish = True
        for neighbor in graph[start]:
            if neighbor not in visited:
                finish = False
                break
        if finish:
            return 100000000
        for neighbor in graph[start]:
            if ids[neighbor-1] == ids[target-1] and neighbor != target:
                ans += 1
                return ans
        ans += min([bfs(graph, ids, visited, target, neighbor) for neighbor in graph[start] if neighbor not in visited]) + 1
    return ans

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    aux = list(filter(lambda x: x == val, ids))
    if len(aux) <= 1:
        return -1
    id = 0
    indices = []
    while id < len(ids):
        if ids[id] == val:
            indices.append(id+1)
        id += 1

    graph = defaultdict(set)
    for i in range(len(graph_from)):
        graph[graph_from[i]].add(graph_to[i])
        graph[graph_to[i]].add(graph_from[i])

    res = [bfs(graph, ids, set(), target, target) for target in indices]

    return min(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

