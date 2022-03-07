from GenericTree import *
import queue
def MaxSumNode(root):
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)
    m = 0
    s = 0
    n = None
    while (not(q.empty())):
        node = q.get()
        s = node.data
        for i in node.children:
            q.put(i)
            s = s + i.data
        if s>=m:
            m = s
            n = node
    return n,m

print(MaxSumNode(root)[0].data)