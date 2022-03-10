from LinkedList import *

def reverseLLIteratively(head):
    if head is None or head.next is None:
        return head
    next = head.next
    prev = head
    while next is not None:
        head.next = next.next
        next.next = prev
        prev = next
        next = head.next
    return prev

head = takeInput()
printLinkedList(reverseLLIteratively(head))