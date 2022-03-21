def lcs(a,b,m,n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if a[i] == b[j]:
                dp[i][j] = 1+dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]


a = input()
b = input()
m = len(a)
n = len(b)
print(lcs(a,b,m,n))