from BinaryTree import *

def postOrderBinaryTree(root):
    if root is None:
        return None
    postOrderBinaryTree(root.left)
    postOrderBinaryTree(root.right)
    print(root.data, end = ' ')

postOrderBinaryTree(root)