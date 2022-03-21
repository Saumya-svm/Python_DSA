from BinaryTree import *

def getMinAndMax(root) :
    if root is None:
        return [2**32-1,0]
    minmax_left = getMinAndMax(root.left)
    minmax_right = getMinAndMax(root.right)
    maxim = max(root.data,max(minmax_left[1],minmax_right[1]))
    minim = min(root.data,min(minmax_right[0],minmax_left[0]))
    return [minim,maxim]

minmax = getMinAndMax(root)
print(minmax[0],minmax[1])