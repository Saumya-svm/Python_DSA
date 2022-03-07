# 'LinkedList' is available in the main folder
from LinkedList import *


def deleteNode(head,i):
    l = lengthOfLL(head)
    if i>=l:
        return head
    if i==0:
        return head.next
    h = head
    c = 0
    prev = None
    while h is not None:
        if c==i:
            prev.next = h.next
            
            break
        else:
            prev = h
            h = h.next
            c+=1




n = int(input())
for i in range(n):
    head = takeInput()
    i = int(input())
    deleteNode(head,i)
    printLinkedList(head)
