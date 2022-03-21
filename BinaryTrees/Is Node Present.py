from BinaryTree import *

def isNodePresent(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    lb = isNodePresent(root.left,x)
    rb = isNodePresent(root.right,x)
    return lb or rb 

x = int(input())
print(isNodePresent(root,x))