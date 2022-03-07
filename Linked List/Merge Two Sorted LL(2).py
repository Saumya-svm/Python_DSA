from LinkedList import *

def mergeLL(head1,head2):
    newHead = None
    newTail = None

    if head1 is None:
        return head2

    if head2 is None:
        return head2

    if head1.data < head2.data:
        newHead = head1
        newTail = head1
        head1 = head1.next

    else:
        newHead = head2
        newTail = head2
        head2 = head2.next

    while (head1 and head2) is not None:
        if head1.data < head2.data:
            newTail.next = head1
            newTail = newTail.next
            head1 = head1.next

        else:
            newTail.next = head2
            newTail = newTail.next
            head2 = head2.next

    if head1 is not None:
        newTail.next = head1
    if head2 is not None:
        newTail.next = head2

    return newHead


t = int(input())
for j in range(t):
    head = []
    for i in range(2):
        head.append(takeInput())
    h = mergeLL(head[0],head[1])
    printLinkedList(h)

