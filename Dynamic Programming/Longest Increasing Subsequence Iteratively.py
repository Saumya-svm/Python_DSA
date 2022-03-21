def lis(l,n):
    dp = [[0 for i in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1,n):
            if l[j]>l[i]:
                including_max = max(including_max,1+dp[j][0])
        excluding_max = dp[i+1][1]
        overall_max = max(including_max,excluding_max)
        dp[i][0] = including_max
        dp[i][1] = overall_max 
    return dp[0][1]

l = list(map(int,input().split()))
n = len(l)
print(lis(l,n))