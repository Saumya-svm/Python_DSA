def ways(n):
    if n==1 or n==0:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return ways(n-1)+ways(n-2)+ways(n-3)
    
n=int(input())
print(ways(n))