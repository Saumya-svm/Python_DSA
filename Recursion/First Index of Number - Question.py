def firstIndex(arr, x,si):
    # Please add your code here
    l=len(arr)
    if si==l:
        return -1
    if arr[si]==x:
        return si
    isFirstIndex=firstIndex(arr,x,si+1)
    return isFirstIndex
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
