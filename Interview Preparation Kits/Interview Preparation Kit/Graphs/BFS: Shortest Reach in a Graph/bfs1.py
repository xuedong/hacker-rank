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
def bfs(graph, visited, distances, starts):
    if starts == []:
        return distances
    nexts = []
    for start in starts:
        visited.add(start)
        if start in graph:
            finish = True
            for neighbor in graph[start]:
                if neighbor not in visited:
                    distances[neighbor-1] = distances[start-1] + 6
                    if neighbor not in nexts:
                        nexts.append(neighbor)
                    finish = False
            if finish:
                break
                    
    distances = bfs(graph, visited, distances, nexts)
    return distances

def find_all_distances(graph_nodes, graph_from, graph_to, start):
    distances = [0] * graph_nodes

    graph = defaultdict(set)
    for i in range(len(graph_from)):
        graph[graph_from[i]].add(graph_to[i])
        graph[graph_to[i]].add(graph_from[i])
    
    distances = bfs(graph, set(), distances, [start])
    for i in range(len(distances)):
        if distances[i] == 0:
            distances[i] -= 1

    return distances


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        graph_nodes, graph_edges = map(int, input().split())

        graph_from = [0] * graph_edges
        graph_to = [0] * graph_edges

        for i in range(graph_edges):
            graph_from[i], graph_to[i] = map(int, input().split())

        start = int(input())

        distances = find_all_distances(graph_nodes, graph_from, graph_to, start)
        for i in range(len(distances)):
            if i != start-1 and i != len(distances)-1:
                print(str(distances[i])+' ', end='')
            elif i != start-1 and i == len(distances)-1:
                print(str(distances[i]))

