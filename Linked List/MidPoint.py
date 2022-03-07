from LinkedList import *

def midpointLL(head):
    fast = head
    slow = head
    if head is None or head.next is None:
        return head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow.data

head = takeInput()
print(midpointLL(head))