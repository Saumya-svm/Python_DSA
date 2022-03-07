def multiplication(a,b):
    if a==0 or b==0:
        return 0
    return multiplication(a,b-1)+a
    
from sys import setrecursionlimit
setrecursionlimit(10**6)    
m,n=int(input()),int(input())
if n>=0:
    x=(multiplication(m,n))
else:
    x=(-1*multiplication(m,-n))
print(x)
