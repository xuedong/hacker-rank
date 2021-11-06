"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head:
        return False
    
    if not head.next:
        return False
    
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        else:
            visited.add(current)
            current = current.next
            
    return False

