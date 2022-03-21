from BinaryTree import *

def nodeGreaterThanX(root,x):
    if root is None:
        return 0
    lcount = nodeGreaterThanX(root.left,x)
    rcount = nodeGreaterThanX(root.right,x)
    if root.data > x:
        return 1+lcount+rcount
    else:
        return lcount+rcount

x = int(input())
print(nodeGreaterThanX(root,x))