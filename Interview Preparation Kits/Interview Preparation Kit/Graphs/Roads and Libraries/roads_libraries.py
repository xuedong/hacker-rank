#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the roadsAndLibraries function below.
def dfs(graph, visited, i):
    visited.add(i)
    ans = 1
    if i in graph:
        for j in graph[i]:
            if j not in visited:
                ans += dfs(graph, visited, j)
    return ans

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return c_lib * n
    
    visited = set()
    graph = defaultdict(set)
    for i, j in cities:
        graph[i].add(j)
        graph[j].add(i)

    return sum((dfs(graph, visited, i) - 1) * c_road + c_lib for i in range(1, n+1) if i not in visited)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

