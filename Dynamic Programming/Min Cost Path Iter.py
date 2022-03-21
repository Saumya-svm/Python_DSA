import sys

def minCostPath(row,col,mat):
    dp = [[sys.maxsize for i in range(col+1)] for j in range(row+1)]

    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if i == row-1 and j == col-1:
                dp[i][j] = mat[i][j]
            else:
                dp[i][j] = mat[i][j] + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
            print(f'i = {i} j = {j} dp[i][j] = {dp[i][j]}')
    return dp[0][0]

def matrixInput():
    m,n = list(map(int,input().split()))
    matrix = []
    for i in range(m):
        matrix.append(list(map(int,input().split())))
    return m,n,matrix


row,col,mat = matrixInput()
dp = [[sys.maxsize for i in range(col+1)] for i in range(row+1)]
print(minCostPath(row,col,mat))