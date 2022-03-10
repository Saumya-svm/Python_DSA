def downHeapify(l,i,n):
    parentIndex = i
    childIndex1 = parentIndex*2+1
    childIndex2 = parentIndex*2+2

    while childIndex1 < n:
        minIndex = parentIndex
        if l[minIndex]>l[childIndex1]:
            minIndex = childIndex1
        if childIndex2<n and l[minIndex]>l[childIndex2]:
            minIndex = childIndex2
        if minIndex == parentIndex:
            return 
        l[minIndex],l[parentIndex] = l[parentIndex],l[minIndex]
        parentIndex = minIndex
        childIndex1 = parentIndex*2+1
        childIndex2 = parentIndex*2+2
    return  

def heapSort(l):
    n = len(l)
    start = n//2 - 1
    for i in range(start,-1,-1):
        downHeapify(l,i,n)

    for i in l:
        print(i,end = ' ')
    
    for i in range(n-1,0,-1):
        l[0],l[i] = l[i],l[0]
        downHeapify(l,0,i)
    return l


l = list(map(int,input().split()))
l = heapSort(l)
for i in l:
    print(i,end = ' ')

