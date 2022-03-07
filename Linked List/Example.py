from LinkedList import lengthOfLL,printLinkedList
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

'''head = Node(1)
h1 = head
head.next = Node(2)
h1.next = Node(3)
print(head.next.data,head.data,head.next.next)'''

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

tail1 = head.next
head.next.next.next = tail1
printLinkedList(head)

