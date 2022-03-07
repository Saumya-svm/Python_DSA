from GenericTree import *

def NodeWithLargestData(root):
    if root is None:
        return None
    maximum = root.data
    for i in root.children:
        maximum = max(NodeWithLargestData(i),maximum)
    return maximum

print(NodeWithLargestData(root))