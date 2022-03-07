from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    rsum = 0
    lsum = 0
    i = 1
    flag = True
    for j in range(1,n):
        lsum+= arr[j]
    while i<n-1:
        rsum=rsum + arr[i-1]
        lsum =lsum -arr[i]
        if rsum == lsum:
            return i
        i=i+1
    if flag == True:
        return -1



#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1