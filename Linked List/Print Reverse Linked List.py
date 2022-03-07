from LinkedList import *

def printReverseLL(head):
    if head == None:
        return
    if head.next == None:
        print(head.data,end = ' ')
        return
    h = printReverseLL(head.next)
    print(head.data,end = ' ')
    return 

head = takeInput()
printReverseLL(head)