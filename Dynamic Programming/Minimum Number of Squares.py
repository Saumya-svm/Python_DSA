from sys import setrecursionlimit
setrecursionlimit(10**6)
import sys

def minStepsTo1(n,dp):
    if n==0:
        return 0
    
    last_square = int(n**0.5)
    count = sys.maxsize
    for i in range(1,last_square+1):
        nc = n-i**2
        if dp[nc] == -1:
            dp[nc] = minStepsTo1(nc,dp)
            steps = 1+dp[nc]
        else:
            steps = 1+dp[nc]
        count = min(count,steps)
    return count 

n = int(input())
dp = [-1]*(n+1)
print(minStepsTo1(n,dp))