from BinaryTree import *

def getSum(root):
    if root is None:
        return 0
    
    lsum = getSum(root.left)
    rsum = getSum(root.right)
    return lsum + rsum + root.data

print(getSum(root))