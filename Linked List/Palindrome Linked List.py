from LinkedList import *

def reverseLL(head) :
    if head is None or head.next == None:
        return head
    rest = reverseLL(head.next)
    head.next.next = head
    head.next = None
    return rest
    
def isPalindrome(head):
    r = reverseLL(head)
    while head is not None:
        if head.data != r.data:
            return False
        head = head.next
        r = r.next
    return True

head = takeInput()
if isPalindrome(head):
    print('true')
else:
    print('false')