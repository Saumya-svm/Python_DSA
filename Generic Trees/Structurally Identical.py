from GenericTree import *

def isIdentical(tree1, tree2):
    if (tree1 or tree2) is None:
        return None
    q1 = queue.Queue()
    q1.put(tree1)
    q2 = queue.Queue()
    q2.put(tree2)
    if tree1.data != tree2.data:
        return False
    
    while (not(q1.empty())) and (not(q2.empty())):
        node1 = q1.get()
        node2 = q2.get()
        l1 = []
        l2 = []
        for i in node1.children:
            l1.append(i.data)
        for i in node2.children:
            l2.append(i.data)
        if l2 != l1:
            return False
    return True
root2 = list(map(int,input().split()))
root2 = inputLevelWise(root2)
print(isIdentical(root,root2))