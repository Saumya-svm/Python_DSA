from sys import setrecursionlimit
sys.setrecursionlimit(10**6)

import sys

def minSquares(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0

    for i in range(1,n+1):
        ans = sys.maxsize()
        root = int(i**0.5)
        for j in range(1,root+1):
            currAns = dp[i-j**2]
            ans = min(ans,currAns)
        dp[i] = ans
    return dp[n]



n = int(input())
print(minSquares(n))