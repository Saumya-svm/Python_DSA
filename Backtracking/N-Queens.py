def isSafe(row,col,board):
    # queen can be attacked from 6 sides-up,down,left,right,right diagonal,left diagnoal
    # but down,right,left will not be checked in this function
    # this is because we have already checked the let positions in the original loop in the helper function
    # right,down because we we will reach there later with the helper functions
    # others will be checked because we might have placed queens before coming to the current position

    i = row-1
    while i>=0:
        if board[i][col] == 1:
            return False
        i-=1
        
    i = row-1
    j = col-1
    while i>=0 and j>=0:
        if board[i][j] ==1:
            return False
        i-=1
        j-=1
        
    i = row-1
    j = col+1
    while i>=0 and j<n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1
        
    return True

def printPathHelper(row,n,board):
    if row>=n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end = ' ')
        print()
        return 

    for col in range(n):
        if isSafe(row,col,board):
            board[row][col] = 1
            printPathHelper(row+1,n,board)
            # printed all the available paths when the current row and col is a safe spot
            # changing the value of that position to 0 for all the recursive calls now as 
            # we search for new paths
            board[row][col] = 0
    
    return

def printPath(n):
    board = [[0 for i in range(n)] for j in range(n)]
    printPathHelper(0,n,board)

n = int(input())
printPath(n)