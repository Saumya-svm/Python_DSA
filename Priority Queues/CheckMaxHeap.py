def checkMaxHeap(arr):
    n = len(arr)
    start = n//2-1
    flag = True
    for i in range(0,start+1):
        parent = arr[i]
        leftIndex = 2*i+1
        rightIndex = 2*i+2
        leftChild = arr[leftIndex]
        if rightIndex < n:
        	rightChild = arr[rightIndex]
        boolLeft = parent > leftChild
        boolRight = parent > rightChild
        if (boolRight and boolLeft) == False:
            return False
    return True
        

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')