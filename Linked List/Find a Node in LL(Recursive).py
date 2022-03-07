from LinkedList import *

def findNode(head,num,n = 0):
    if head is None:
        return -1
    if num == head.data:
        return n
    
    bool = findNode(head.next,num,n+1)
    return bool

head = takeInput()
num = int(input())
print(findNode(head,num))