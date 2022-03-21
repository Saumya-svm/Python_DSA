from BinaryTree import *

def mirrorBinaryTree(root):
    if root is None:
        return None
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    root.right,root.left = root.left,root.right

def printLevelWise(root):
    if root==None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ

mirrorBinaryTree(root)
printLevelWise(root)
