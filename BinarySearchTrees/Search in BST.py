import sys

sys.path.insert(1, '/Users/saumyamundra/Documents/CodingNinjas_PythonDSA/BinaryTrees')

from BinaryTree import *

def elementsInRangeK1K2(root,k1,k2,l = []):
    if root is None:
        return None
    if root.data < k1:
        return elementsInRangeK1K2(root.right,k1,k2,l)
    if root.data > k2:
        return elementsInRangeK1K2(root.left,k1,k2,l)
    
    else:
        l.append(root.data)
        elementsInRangeK1K2(root.left,k1,k2,l)
        elementsInRangeK1K2(root.right,k1,k2,l)
        return l

k1,k2 = list(map(int,input().split()))
print(elementsInRangeK1K2(root,k1,k2))
