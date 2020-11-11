class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    if root:
        node_queue = [root]
        level_dict = dict()
        level = 0
        root.level = 0
        
        while len(node_queue):
            current = node_queue[0]
            level = current.level
            if level not in level_dict:
                level_dict[level] = current.info
            if current.left:
                current.left.level = level - 1
                node_queue.append(current.left)
            if current.right:
                current.right.level = level + 1
                node_queue.append(current.right)
            node_queue.pop(0)
        
        for i in sorted(level_dict):
            print(str(level_dict[i]), end=" ")

