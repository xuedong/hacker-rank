#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def in_graph(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    return i >= 0 and j >= 0 and i < n and j < m

def dfs(grid, visited, i, j):
    visited.add((i, j))
    ans = 1
    neighbors = [(i-1, j-1), (i, j-1), (i-1, j), (i+1, j-1), (i-1, j+1), (i, j+1), (i+1, j), (i+1, j+1)]
    for (x, y) in neighbors:
        if in_graph(grid, x, y) and (x, y) not in visited and grid[x][y] == 1:
            ans += dfs(grid, visited, x, y)
    return ans

def max_region(grid):
    visited = set()
    n = len(grid)
    m = len(grid[0])
    max_value = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i, j) not in visited:
                ans = dfs(grid, visited, i, j)
                max_value = max(max_value, ans)
    
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = max_region(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

