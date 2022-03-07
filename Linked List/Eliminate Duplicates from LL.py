from os import remove
from LinkedList import *

def removeDuplicates(head):
    h = head
    prev = None
    while h.next is not None:
        if h.data!=h.next.data:
            prev = h
            h = h.next
        else:
            prev = prev
            h.next = h.next.next

    return head

head = takeInput()
printLinkedList(removeDuplicates(head))