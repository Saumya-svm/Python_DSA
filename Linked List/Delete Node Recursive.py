from LinkedList import *

def deleteNode(head,i,n):
    if i>lengthOfLL(head):
        return head
    
    if n==i:
        return head.next

    head.next = deleteNode(head.next,i,n+1)


head = takeInput()
i = int(input())
head = deleteNode(head,i,0)
printLinkedList(head)