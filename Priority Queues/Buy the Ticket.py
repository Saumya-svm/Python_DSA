import heapq

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
    
    def print(self):
        h = self.head
        while h is not None:
            print(h.data)
            h = h.next

    def dequeue(self):
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    

def buyTicket(l,k):
    q = Queue()
    for i in range(len(l)):
        q.enqueue(i)
    arr = l[0:]
    heapq._heapify_max(arr)
    time = 0
    while True:
        if l[q.peek()]<arr[0]:
            x = q.dequeue()
            q.enqueue(x)
        if l[q.peek()] == arr[0]:
            time+=1
            if q.peek() == k:
                return time
            x = q.dequeue()
            arr = arr[1:]
            heapq._heapify_max(arr)


l = list(map(int,input().split()))
k = int(input())
time = buyTicket(l,k)
print(time)