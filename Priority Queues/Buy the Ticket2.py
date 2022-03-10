from sys import stdin
import sys
import heapq as heap

class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data
    def print(self):
        h = self.head
        while h is not None:
            print(h.data)
            h = h.next
    
def buyTicket(arr, n, k) : 
    li=arr[0:]
    heap._heapify_max(li)
    q=Queue()
    for i in range(len(arr)):
        q.enqueue(i)
    bool=True
    count=0
    while bool:
        if [q.peek()]<li[0]:
            x=q.dequeue()
            q.enqueue(x)
        if q.peek()==li[0]:
            count+=1
            if q.peek()==k:
                bool==False
                return count
            heap._heappop_max(li)
            q.dequeue()
        print(li,count)
        q.print()


#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print(buyTicket(arr, n, k))