import heapq 
def kthLargest(lst, k): 
    minHeap = [] 
    heapq.heapify(minHeap)
    n = len(lst) 
    for i in range(0,k): 
        heapq.heappush(minHeap,lst[i])
        # Add first k elements to min heap 
    for i in range(k,n): 
        if lst[i]>minHeap[0]: 
            heapq.heappop(minHeap) 
            heapq.heappush(minHeap, lst[i]) 
    return minHeap[0]

l = list(map(int,input().split()))
k = int(input())
ans = kthLargest(l,k)
print(ans)