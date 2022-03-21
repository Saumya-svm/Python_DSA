from BinaryTree import *

def insertDuplicateNode(root):
    if (root) is None:
        return None
    a = root.left 
    b = root.right
    root.left = root
    left = insertDuplicateNode(a)
    right = insertDuplicateNode(b)
    root.left.left = left
    root.right = right
    return root

printLevelWise(insertDuplicateNode(root))