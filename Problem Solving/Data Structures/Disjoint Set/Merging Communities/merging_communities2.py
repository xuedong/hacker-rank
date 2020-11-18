# Union-Find with union by size and find by path compression
#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.size = 1
        
def make_set(data):
    return Node(data)

def find(node):
    if node != node.parent:
        node.parent = find(node.parent)
    return node.parent

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    
    if root1 != root2:
        if root1.size < root2.size:
            root1, root2 = root2, root1
        root2.parent = root1
        root1.size += root2.size
    

if __name__ == '__main__':
    number, queries = map(int, input().split())
    dsf = [make_set(i) for i in range(1, number+1)]
    
    for _ in range(queries):
        query = input().split()
        if len(query) == 2:
            node = int(query[1])
            print(find(dsf[node-1]).size)
        else:
            node1, node2 = map(int, query[1:])
            union(dsf[node1-1], dsf[node2-1])
            
