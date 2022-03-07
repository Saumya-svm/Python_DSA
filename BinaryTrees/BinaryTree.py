import queue

class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    
def takeInput():
    levelInput = list(map(int,input().split()))
    
    length = len(levelInput)
    start = 0
    if length == 0:
        return None
    root = BinaryTreeNode(levelInput[0])
    q = queue.Queue()
    q.put(root)

    start+=1
    while not q.empty():
        currentNode = q.get()
        leftChild = levelInput[start]
        start+=1

        if leftChild!=-1:
            leftChildNode = BinaryTreeNode(leftChild)
            currentNode.left = leftChildNode
            q.put(leftChildNode)

        rightChild = levelInput[start]
        start+=1

        if rightChild!=-1:
            rightChildNode = BinaryTreeNode(rightChild)
            currentNode.right = rightChildNode
            q.put(rightChildNode)

    return root

def printLevelWise(root):
    if root is None:
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

root = takeInput()