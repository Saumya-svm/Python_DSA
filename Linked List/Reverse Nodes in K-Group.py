from LinkedList import *

def reverseNodesInKGroup(head,k):
    if head is None:
        return None
    curr = head
    for i in range(k):
        if curr is None:
            return head
        curr = curr.next
    next = head.next
    prev = head
    for _ in range(k-1):
        head.next = next.next
        next.next = prev
        prev = next
        next = head.next
    head.next = reverseNodesInKGroup(head.next,k)
    return prev

head = takeInput()
k = int(input())
printLinkedList(reverseNodesInKGroup(head,k))