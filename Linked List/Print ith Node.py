# 'LinkedList' is available in the main folder
from LinkedList import *

def print_ith(head,i):
    h = head
    c = 0
    while h is not None:
        if c==i:
            print(h.data)
            break
        h = h.next
        c+=1


n = int(input())
for i in range(n):
    head = takeInput()
    i = input()
    print_ith(head,i)
