from LinkedList import *

def evenAfterOdd(head):
    if head is None:
        return head
    oddHead = None
    evenHead = None

    evenTail = None
    oddTail = None

    while head is not None:
        if head.data % 2 == 0:
            if evenHead == None:
                evenHead = head
                evenTail = head
            else:
                evenTail.next = head
                evenTail = evenTail.next
        elif head.data%2 == 1:
            if oddHead == None:
                oddHead = head
                oddTail = head
            else:
                oddTail.next = head
                oddTail = oddTail.next
        head = head.next
    
    if oddHead is None:
        return evenHead
    else:
        oddTail.next = evenHead
    if evenTail is not None:
        evenTail.next = None

    return oddHead

head = takeInput()
printLinkedList(evenAfterOdd(head))
