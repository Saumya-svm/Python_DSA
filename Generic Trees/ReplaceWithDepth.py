from GenericTree import *
import queue
def replacewithDepth(root):
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)
    root.data = 0
    while (not(q.empty())):
        node = q.get()
        for i in node.children:
            q.put(i)
            i.data = node.data + 1
    return root

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

print(printLevelAtNewLine(replacewithDepth(root)))