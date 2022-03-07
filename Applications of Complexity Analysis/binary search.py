def binarySearch(lst,ele,start = 0,end = 0):
    start = 0
    end = len(lst) - 1
    mid = (start+end)//2
    if start>=end:
        return False
    if mid == ele:
        return True
    bool1 = binarySearch(lst,ele,start,mid-1)
    bool2 = binarySearch(lst,ele,mid+1,end)
    return bool1 or bool2

print(binarySearch([i for i in range(20)],13))