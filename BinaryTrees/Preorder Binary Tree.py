from BinaryTree import *

def preOrderBinaryTree(root):
    if root is None:
        return None
    print(root.data, end = ' ')
    preOrderBinaryTree(root.left)
    preOrderBinaryTree(root.right)

preOrderBinaryTree(root)