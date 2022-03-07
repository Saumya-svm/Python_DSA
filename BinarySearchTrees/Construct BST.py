class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def constructBST(list):
    length = len(list)
    if length == 0:
        return None
    mid = (length-1)//2
    root = BinaryTreeNode(list[mid])
    if mid == 0:
        return root
    print(root.data)
    leftTree = constructBST(list[:mid])
    rigthTree = constructBST(list[mid+1:])
    root.left = leftTree
    root.right = rigthTree
    return root 

def preOrder(root):
    if root is None:
        return None
    print(root.data,end = ' ')
    preOrder(root.left)
    preOrder(root.right)

#n = int(input())
#list = list(map(int,input().split()))
list = [i for i in range(1,8)]
preOrder(constructBST(list))
