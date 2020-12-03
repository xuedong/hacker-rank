""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if not(root):
        return True
    
    if not(root.left) and not(root.right):
        return True
    
    if not(root.left):
        current = root.right
        while current:
            if not(current.left):
                left_most = current.data
            current = current.left
        return left_most > root.data and checkBST(root.right)
    
    if not(root.right):
        current = root.left
        while current:
            if not(current.right):
                right_most = current.data
            current = current.right
        return right_most < root.data and checkBST(root.left)
    
    current_right = root.right
    while current_right:
        if not(current_right.left):
            left_most = current_right.data
        current_right = current_right.left
    current_left = root.left
    while current_left:
        if not(current_left.right):
            right_most = current_left.data
        current_left = current_left.right
            
    return left_most > root.data and right_most < root.data and checkBST(root.right) and checkBST(root.left)

