class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeInput():
    head = None
    tail = None

    values = list(map(int,input().split()))
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

def printLinkedList(head):
    h = head
    while h is not None:
        print(h.data)
        h = h.next

def lengthOfLL(head):
    c = 0
    while head is not None:
        c+=1
        head = head.next

    return c