from BinaryTree import *

def printNodesAtDepthK(root,k):
    if root is None:
        return 
    if k==0:
        print(root.data,end = ' ')
        return 

    printNodesAtDepthK(root.left,k-1)
    printNodesAtDepthK(root.right,k-1)

k = int(input())
printNodesAtDepthK(root,k)