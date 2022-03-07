from GenericTree import *

def countLeafNodes(root):
    if root is None:
        return
    if len(root.children) == 0:
        return 1
    c = 0
    for i in root.children:
        c += countLeafNodes(i)
    return c 


print(countLeafNodes(root))
