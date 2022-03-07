from LinkedList import *

def length(head):
    if head is None:
        return 0
    l = length(head.next)
    return l+1

head = takeInput()
print(length(head))