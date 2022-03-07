import queue
class TreeNode():
    def __init__(self,data):
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root

def sumOfNodes(root):
    if root is None:
        return None
    s = root.data
    for i in root.children:
        s+= sumOfNodes(i)
    return s

li = list(map(int,input().split()))
root = inputLevelWise(li)
print(sumOfNodes(root))