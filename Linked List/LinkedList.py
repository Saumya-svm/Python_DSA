class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeInput():
    values = list(map(int,input().split()))
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

def printLinkedList(head):
    h = head
    while h is not None:
        print(h.data, end = ' ')
        h = h.next
    print()

def lengthOfLL(head):
    c = 0
    while head is not None:
        c+=1
        head = head.next

    return c

# will return the middle node
def midpointLL(head):
    fast = head
    slow = head
    if head is None or head.next is None:
        return head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow