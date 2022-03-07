from GenericTree import *

def containsX(root,x):
    if root is None:
        return None
    flag = False
    if root.data == x:
        return True
    q = queue.Queue()
    q.put(root)
    while (not(q.empty())):
        node = q.get()
        if node.data == x:
            return True
        for i in node.children:
            q.put(i)
            if i.data == x:
                return True
    return False


x = int(input())
print(containsX(root,x))