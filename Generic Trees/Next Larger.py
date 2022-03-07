from GenericTree import *
import queue
def nextLarger(root,x):
    q = queue.Queue()
    q.put(root)
    l = []
    while  (not q.empty()):
        node = q.get()
        if node.data>x:
            l.append(node.data)
        for i in node.children:
            q.put(i)
    return l

x = int(input())
print(min(nextLarger(root,x)))