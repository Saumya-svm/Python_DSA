def binarySearch(lst,ele,start = 0,end = 0):
    start = 0
    end = len(lst) - 1
    mid = (start+end)//2
    if mid == ele:
        return True
    bool1 = binarySearch(lst,ele,start,mid-1)
    bool2 = binarySearch(lst,ele,mid+1,end)
    return bool1 or bool2

        

def pairSum(l,num):
    pair_list = []
    for i in l:
        if num-l>0:
            if binarySearch(l,num-i):
                pair_list.append([i,num-i])

l = list(map(int,input().split()))
num = int(input())
print(pairSum(l,num))