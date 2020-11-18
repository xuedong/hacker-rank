# Naive solution
#!/bin/python3
from collections import defaultdict

if __name__ == '__main__':
    nq = input().split()
    number = int(nq[0])
    queries = int(nq[1])
    
    graph = defaultdict(set)
    for i in range(1, number+1):
        graph[i].add(i)
    
    for i in range(queries):
        query = input().split()
        if len(query) == 2:
            node = int(query[1])
            print(len(graph[node]))
        else:
            node1 = int(query[1])
            node2 = int(query[2])
            if node1 in graph[node2]:
                continue
            else:
                graph[node1] = graph[node1].union(graph[node2])
                for node in graph[node1]:
                    graph[node] = graph[node1]
            
