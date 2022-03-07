from LinkedList import *

def AppendLastNToFirst(head,n):
    if n == 0 or head is None:
        return head
    
    lastTail = head
    firstTail = head
    originalHead = head

    for i in range(n):
        lastTail = lastTail.next

    while lastTail.next is not None:
        lastTail = lastTail.next
        firstTail = firstTail.next
    head = firstTail.next
    firstTail.next = None
    lastTail.next = originalHead

    return head


            



head = takeInput()
n = int(input())
printLinkedList(AppendLastNToFirst(head,n))

