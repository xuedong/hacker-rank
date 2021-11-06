#!/bin/python3
import queue
from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(set)

    def connect(self, node_x, node_y):
        self.edges[node_x].add(node_y)
        self.edges[node_y].add(node_x)

    def find_all_distances(self, start):
        distances = [-1] * self.nodes
        unvisited = set([i for i in range(self.nodes)])
        q = queue.Queue()

        distances[start] = 0
        unvisited.remove(start)
        q.put(start)
        while not q.empty():
            current_node = q.get()
            children = self.edges[current_node]
            current_depth = distances[current_node]
            for child in children:
                if child in unvisited:
                    distances[child] = current_depth + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(start)

        print(" ".join(map(str, distances)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)

