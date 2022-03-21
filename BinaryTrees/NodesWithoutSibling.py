from BinaryTree import *

def printNodesWithoutSibling(root) :
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data,end = ' ')
        printNodesWithoutSibling(root.left)
    if root.left is None and root.right is not None:
        print(root.right.data, end = ' ')
        printNodesWithoutSibling(root.right)
    if root.left is not None and root.right is not None:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)
    
printNodesWithoutSibling(root)