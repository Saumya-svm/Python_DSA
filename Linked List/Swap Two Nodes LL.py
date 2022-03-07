from LinkedList import *

def swapNodes(head,i,j):
    temp = head
    ith_ele = jth_ele = c = 0
    ith_tail =ith_head =  jth_head = jth_tail = None
    while temp is not None:
        if c == i:
            ith_ele = temp
            ith_head = temp.next
        if c == j:
            jth_ele = temp
            jth_head = temp.next
        if c<i:
            ith_tail = temp
        if c<j:
            jth_tail = temp
        temp = temp.next
        c+=1
    
    ith_tail.next = ith_ele
    ith_ele.next = ith_head
    jth_tail.next = jth_ele
    jth_ele.next = jth_head
    print(ith_ele.data,jth_ele.data)
    printLinkedList(ith_head)
    printLinkedList(jth_head)
    return head

    
head = takeInput()
i,j = list(map(int,input().split()))
printLinkedList(swapNodes(head,i,j))