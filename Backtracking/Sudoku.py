def presentInRow(board,row,num):
    for j in range(9):
        if board[row][j] == num:
            return True
        return False

def presentInCol(board,col,num):
    for j in range(9):
        if board[j][col] == num:
            return True
        return False

def presentInBox(board,row,col,num):
    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j] == num:
                return True
    return False

def isPossible(board,row,col,num):
    if presentInRow(board,row,num):
        return False
    if presentInCol(board,row,num):
        return False
    if presentInBox(board,row-row%3,col-col%3,num):
        return False

def solveSudoku(board):
    row = -1
    col = -1
    flag = False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row = i
                col = j
                flag = True
                break
        if flag:
            break
    
    if row == -1:
        return True
    for num in range(1,10):
        if isPossible(board,row,col,num):
            board[row][col] = num
            if solveSudoku(board):
                return True
            board[row][col] = 0
    return False



board = [[int(i) for i in input().split()]for j in range(9)]
if solveSudoku(board):
    print('True')
else:
    print('false')
