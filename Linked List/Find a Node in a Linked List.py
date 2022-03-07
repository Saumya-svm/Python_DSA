from LinkedList import *

def findNode(head,i):
    h = head
    c = 0
    while h is not None:
        if h.data == i:
            return c
        h = h.next
        c+=1

head = takeInput()
i = int(input())
print(findNode(head,i))