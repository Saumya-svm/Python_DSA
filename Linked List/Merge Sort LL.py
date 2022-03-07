from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def merge(head1,head2):

    fh = Node(3)
    ft = fh       
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next
            
    while head1 is not None:
        ft.next = head1
        ft = ft.next
        head1 = head1.next
    
    while head2 is not None:
        ft.next = head2
        ft = ft.next    
        head2 = head2.next
    
    return fh.next

def midpoint_linkedlist(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def mergeSort(head):
    if head is None:
        return head
    if head.next is None:
      return head

    mid = midpoint_linkedlist(head)

    h1 = head
    temp = head
    while temp is not mid:
        temp = temp.next
    h2 = temp.next       
    temp.next = None
    h1 = mergeSort(h1)
    h2 = mergeSort(h2)
    
    return merge(h1, h2)




#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(input())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1