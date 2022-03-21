from BinaryTree import *

def replaceNodeWithDepthK(root,k=0):
    if root is None:
        return None
    root.data = k
    leftChild = replaceNodeWithDepthK(root.left,k+1)
    rightChild = replaceNodeWithDepthK(root.right,k+1)
    root.left = leftChild
    root.right = rightChild
    return root

def inOrder(root) :
	if root is None :
		return 

	inOrder(root.left)
	print(root.data, end = " ")
	inOrder(root.right)
	
root = replaceNodeWithDepthK(root)
inOrder(root)
