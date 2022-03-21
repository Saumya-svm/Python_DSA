from BinaryTree import *
def printLevelWise(node):
    if node==None:
        return None
    q=queue.Queue()
    q.put(node)
    while not (q.empty()):
        a=q.get()
        print(a.data,end=":L:")
        if a.left!=None:
            q.put(a.left)
            print(a.left.data,end=",R:")
        else:
            print("-1",end=",R:")
        if a.right!=None:
            q.put(a.right)
            print( a.right.data)
        else:
            print("-1")

printLevelWise(root)