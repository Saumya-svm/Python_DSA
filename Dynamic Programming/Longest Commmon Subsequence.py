# dp is the array which stores the lcs for each substring 
def lcs(a,b,m,n,i,j,dp):
    if i == len(a) or j == len(b):
        return 0 

    if a[i]!=b[j]:
        if dp[i+1][j] == -1:
            ans1 = lcs(a,b,m,n,i+1,j,dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]
        if dp[i][j+1] == -1:
            ans2 = lcs(a,b,m,n,i,j+1,dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
        return max(ans1,ans2)
    else:
        if dp[i+1][j+1] == -1:
            ans = lcs(a,b,m,n,i+1,j+1,dp)
            dp[i+1][j+1] = ans
        else:
            ans = dp[i+1][j+1]
        return 1+ans

        
    

a = input()
b = input()
m = len(a)
n = len(b)
dp = [[-1 for i in range(n+1)] for j in range(m+1)]
print(lcs(a,b,m,n,0,0,dp))