from GenericTree import *

def heightOfTree(root):
    if root is None:
        return None
    height = 0
    for i in root.children:
        height = max(height,heightOfTree(i))
    return height + 1


print(heightOfTree(root))