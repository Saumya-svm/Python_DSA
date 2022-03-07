# sorted in descending order 
def merge(l1,l2):
    i = j = 0
    arr = []
    while i <len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            arr.append(l1[i])
            i=i+1
        elif l1[i] < l2[j]:
            arr.append(l2[j])
            j=j+1
        elif l1[i] == l2[j]:
            arr.append(l1[i])
            arr.append(l2[j])
            i+=1
            j+=1
    
    while i <len(l1):
        arr.append(l1[i])
        i+=1
    while j<len(l2):
        arr.append(l2[j])
        j+=1
    return arr


def mergeSort(l):
    if len(l) == (1 or 0):
        return l
    mid = len(l)//2
    l1 = l[:mid]
    l2 = l[mid:]
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    sorted = merge(l1,l2)
    return sorted


l = list(map(int,input().split()))
sortedList = mergeSort(l)
print(sortedList)
#  for ascending we can either keep an index counter in the merge
# function of reverse the list as shown below
# print(sortedList[::-1])