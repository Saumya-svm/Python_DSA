def sumArray(arr):
    if len(arr)==1:
        return arr[0]
    s=sumArray(arr[1:])
    return s+arr[0]

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))