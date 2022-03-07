
from sys import stdin


#Following is the structure of the node class for a Singly Linked List
'''
    Time complexity: O(q)
    Space complexity: O(q)

    Where q is the number of queries.
'''

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
class Queue:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
        
    # Function to check if the queue is empty.
    def isEmpty(self):
        
        return self.size == 0
    
    def enqueue(self, data):
        
        # Increase the count of elements present in the List.
        self.size += 1
        
        # Create a new node.
        newNode = Node(data)
        
        # Check if the Queue is empty.
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return 
        
        # Push the element to the last of the queue.
        self.tail.next = newNode
        self.tail = newNode
        return 
    
    def dequeue(self):
        
        # Check if the queue is empty.
        if self.isEmpty():
            return -1
        
        ans = self.head.data
        
        tmp = Node(self.head)
        self.head = self.head.next
        
        # If the queue is empty make the tail pointer null.
        if self.head == None:
            self.tail = None
            
        tmp = None
        self.size -= 1
        
        return ans
    
    def front(self):
        
        # Check if the queue is empty.
        if self.isEmpty():
            return -1
        
        # Return the element at the front.
        return self.head.data
    def getSize(self):
        return self.size
        
        
        
            
#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1