def knapsack(weights,values,weight,n):
    dp = [[0 for i in range(weight+1)] for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(weight+1):
            if weight[i] > j:
                ans = dp[i-1][j]
            else:
                ans1 = dp[i-1][j]
                ans2 = values[i-1]+dp[i-1][j-weight[i-1]]
                ans = max(ans1,ans2)
            dp[i][j] = ans
    return dp[n][weight]


def takeInput():
    n = int(input())
    if n==0:
        return [],[],0,n

    weights = list(map(int,input().split()))
    values = list(map(int,input().split()))
    weight = int(input())
    return weights,values,weight,n

weights,values,weight,n = takeInput()
print(knapsack(weights,values,weight,n))