import sys

from numpy import matrix

def minCostPath(i,j,row,col,mat,dp):
    if i>=row or j>=col:
        return sys.maxsize
    if i==row-1 and j==col-1:
        return mat[i][j]

    if dp[i+1][j] == sys.maxsize:
        cost1 = minCostPath(i+1,j,row,col,mat,dp)
        dp[i+1][j] = cost1
    else:
        cost1 = dp[i+1][j]
    if dp[i][j+1] == sys.maxsize:
        cost2 = minCostPath(i,j+1,row,col,mat,dp)
        dp[i][j+1] = cost2
    else:
        cost2 = dp[i][j+1]
    if dp[i+1][j+1] == sys.maxsize:
        cost3 = minCostPath(i+1,j+1,row,col,mat,dp)
        dp[i+1][j+1] = cost3
    else:
        cost3 = dp[i+1][j+1]

    ans = mat[i][j] + min(cost1,cost2,cost3)
    return ans

def matrixInput():
    m,n = list(map(int,input().split()))
    matrix = []
    for i in range(m):
        matrix.append(list(map(int,input().split())))
    return m,n,matrix


row,col,mat = matrixInput()
dp = [[sys.maxsize for i in range(col+1)] for i in range(row+1)]
print(minCostPath(0,0,row,col,mat,dp))