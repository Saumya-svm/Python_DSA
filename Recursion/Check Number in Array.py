def checkNumber(arr, x):
    # Please add your code here
    size=len(arr)
    if size==1:
        return x==arr[0]
    smallAns=checkNumber(arr[:size-1],x)
    return smallAns or x==arr[size-1]
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
