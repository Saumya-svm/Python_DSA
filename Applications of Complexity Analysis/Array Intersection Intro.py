def power(x, n):
    if n==0:
        return 1
    smallPower = power(x,n//2)
    if n%2==0:
        return smallPower*smallPower
    else:
        return x*smallPower*smallPower
    return x*power(x,n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(map(int,input().split()))
print(power(x, n))
