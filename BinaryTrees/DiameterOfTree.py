from BinaryTree import *

def diameterOfTree(root):
    if root is None:
        return 0,0
    lh,ld = diameterOfTree(root.left)
    rh,rd = diameterOfTree(root.right)
    lrd = 1+lh+rh
    h = 1+max(lh,rh)
    return h,max(lrd,max(ld,rd))

print(diameterOfTree(root)[1])