def longestIncreasingSubsequence(l):
    pass

l = list(map(int,input().split()))
n = len(l)
dp = [-1 for i in range(n)]
print(longestIncreasingSubsequence(l,0,n,dp))