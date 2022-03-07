from LinkedList import *

def takeList(values):
    #values = list(map(int,input().split()))
    head = None
    tail = None
    i = 0
    while i<len(values) and values[i]!=-1:
        newNode = Node(values[i])

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
        
        i+=1

    return head

def mergeLL(head1,head2):
    l= []
    while (head1 and head2) is not None:
        if head1.data<head2.data:
            l.append(head1.data)
            head1 = head1.next
        elif head1.data>head2.data:
            l.append(head2.data)
            head2 = head2.next
        else:
            l.append(head1.data)
            l.append(head2.data)
            head1 = head1.next
            head2 = head2.next
    
    if head1 == None:
        while head2 is not None:
            l.append(head2.data)
            head2 = head2.next

    if head2 == None:
        while head1 is not None:
            l.append(head1.data)
            head1 = head1.next

    return takeList(l)




t = int(input())
for j in range(t):
    head = []
    for i in range(2):
        head.append(takeInput())
    h = mergeLL(head[0],head[1])
    printLinkedList(h)

