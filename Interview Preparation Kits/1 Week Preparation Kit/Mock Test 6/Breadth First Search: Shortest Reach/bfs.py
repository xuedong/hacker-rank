#!/usr/bin/env python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n

    queue = [[s, 0]]
    visited[s-1] = True

    ans = [-1] * n
    while queue:
        node, level = queue.pop(0)

        for neighbor in graph[node]:
            if not visited[neighbor-1]:
                visited[neighbor-1] = True
                queue.append([neighbor, level+6])
                ans[neighbor-1] = level + 6

    return ans[:s-1] + ans[s:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

