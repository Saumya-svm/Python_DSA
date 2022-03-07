def quickSort(l,s,e):
    if s>=e:
        return 

    pivot_index = partition(l,s,e)
    quickSort(l,s,pivot_index-1)
    quickSort(l,pivot_index+1,e)

def partition(l,s,e):
    pivot = l[s]
    c=0
    for i in range(s,e+1):
        if l[i] < pivot:
            c+=1
    
    l[s+c],l[s] = l[s],l[s+c]
    pivot_index = s+c
    i = s
    j = e
    while i<j:
        if l[i]<pivot:
            i = i + 1
        elif l[j]>=pivot:
            j = j - 1
        else:
            l[i],l[j] = l[j],l[i]
            i = i + 1
            j = j - 1
    return pivot_index



    

l = list(map(int,input().split()))
quickSort(l,0,len(l)-1)
print(l)