#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def bfs(grid, start, goal):
    m = len(grid)
    n = len(grid[0])
    visited = {}
    queue = []

    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.pop(0)

        x, y = current
        i = x+1
        while i < m:
            if grid[i][y] == 'X':
                break
            if (i, y) not in visited:
                queue.append((i, y))
                visited[(i, y)] = visited[current] + 1
            i += 1
        i = x-1
        while i >= 0:
            if grid[i][y] == 'X':
                break
            if (i, y) not in visited:
                queue.append((i, y))
                visited[(i, y)] = visited[current] + 1
            i -= 1
        j = y+1
        while j < n:
            if grid[x][j] == 'X':
                break
            if (x, j) not in visited:
                queue.append((x, j))
                visited[(x, j)] = visited[current] + 1
            j += 1
        j = y-1
        while j >= 0:
            if grid[x][j] == 'X':
                break
            if (x, j) not in visited:
                queue.append((x, j))
                visited[(x, j)] = visited[current] + 1
            j -= 1

    return visited[goal]
 
def minimumMoves(grid, startX, startY, goalX, goalY):
    start = startX, startY
    goal = goalX, goalY
    return bfs(grid, start, goal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

