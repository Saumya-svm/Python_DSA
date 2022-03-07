import sys

sys.path.insert(1, '/Users/saumyamundra/Documents/CodingNinjas_PythonDSA/BinaryTrees')

from BinaryTree import *
def minTree(root):
    if root is None:
        return 10000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin,rightmin,root.data)

def maxTree(root):
    if root is None:
        return -10000
    leftmax = maxTree(root.left)
    rightmax = maxTree(root.right)
    return max(leftmax,rightmax,root.data)




def checkIsBST(root):
    if root is None:
        return None
    
    leftMax = maxTree(root.left)
    rigthMin = minTree(root.right)
    if root.data>rigthMin and root.data<=leftMax:
        return False
    
    isLeftBST = checkIsBST(root.left)
    isRightBST = checkIsBST(root.right)
    return isLeftBST and isRightBST

ans = checkIsBST(root)
if ans:
    print('true')
else:
    print('false')