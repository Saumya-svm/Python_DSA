from BinaryTree import *

def numberOfLeafNOdes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    lcount = numberOfLeafNOdes(root.left)
    rcount = numberOfLeafNOdes(root.right)
    return lcount+rcount

print(numberOfLeafNOdes(root))