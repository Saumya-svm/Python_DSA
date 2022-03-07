from GenericTree import *

def printLevelWiseTree(root):
    q = queue.Queue()
    if root is None:
        return None
    q.put(root)
    while (not(q.empty())):
        node = q.get()
        print(node.data,end=':')
        for i in node.children:
            q.put(i)
            if node.children.index(i) == len(node.children) - 1:
                print(i.data,end='')
            else:
            	print(i.data,end=',')
        print()

    return 
        

print(printLevelWiseTree(root))