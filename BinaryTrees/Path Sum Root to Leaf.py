from BinaryTree import *

def rootToLeafPathsSumToKHelper(root,k,path,currsum):
    if root is None:
        return
    if (root.left is None) and (root.right is None):
        currsum += root.data
        
        if currsum == k :
            print(str(path + str(root.data)+ ' ').lstrip())

        
    rootToLeafPathsSumToKHelper(root.left,k,str(path + str(root.data)+ ' '),(currsum + root.data))
    rootToLeafPathsSumToKHelper(root.right,k,str(path + str(root.data)+ ' '),(currsum + root.data))

def rootToLeafPathsSumToK(root, k):
    rootToLeafPathsSumToKHelper(root,k,'',0)

k = int(input())
rootToLeafPathsSumToK(root,k)