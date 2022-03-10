import heapq
def kSmallest(l, k):
    heap = l[:k]
    n = len(l)
    heapq._heapify_max(heap)
    for i in range(k,n):
        if heap[0] > l[i]:
            heapq._heapreplace_max(heap,l[i])
	
    return heap

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')