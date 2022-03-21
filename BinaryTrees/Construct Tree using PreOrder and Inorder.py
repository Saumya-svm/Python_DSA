import queue
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def buildTree(pre, inorder) :
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexinorder = -1
    for i in range(len(inorder)):
        if inorder[i] == rootData:
            rootIndexinorder = i
            break
    if rootIndexinorder == -1:
        return None
    li = inorder[0:rootIndexinorder]
    ri = inorder[rootIndexinorder+1:]
    lp = pre[1:len(li)+1]
    rp = pre[len(li)+1:]
    leftTree = buildTree(lp,li)
    rightTree = buildTree(rp,ri)
    
    root.left = leftTree
    root.right = rightTree
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

pre = list(map(int,input().split()))
inorder = list(map(int,input().split()))
printLevelWise(buildTree(pre,inorder))