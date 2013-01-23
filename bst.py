"""
Construct a binary search tree.
But you first need to construct a root. Then insert the rest. 
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    
def search(node, x):
    while node:
        if node.data == x: return True
        elif node.data < x:
            node = node.right
        else:
            node = node.left
    return False

def insert(node, x):                    # return "Node"
    if node is None: return Node(x)
    elif x == node.data: return node
    elif x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node

    
def search_min(node):
    if node.left is None: return node.data
    return search_min(node.left)

def delete_min(node):                   # simulate this, to understand
    if node.left is None: return node.right
    node.left = delete_min(node.left)
    return node

def delete(node,x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete_min(node.right)
        elif x < node.data:
            node.left = delete(node.left, x)
        else:
            node.right = delete(node.right, x)
