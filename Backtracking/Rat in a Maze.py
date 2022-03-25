def printPathHelper(row,col,n,maze,solution):
    # base cases
    if row <0 or col<0 or row>=n or col>=n or maze[row][col] == 0 or solution[row][col] == 1:
        return 

    if row == n-1 and col == n-1:
        solution[row][col] = 1
        print('one more solution found')
        print(solution)
        return

    solution[row][col] = 1
    print(row,col,solution)
    printPathHelper(row+1,col,n,maze,solution)
    printPathHelper(row,col+1,n,maze,solution)
    printPathHelper(row-1,col,n,maze,solution)
    printPathHelper(row,col-1,n,maze,solution)
    solution[row][col] = 0
    return 

def printPath(n,maze):
    solution = [[0 for i in range(n)] for j in range(n)]
    printPathHelper(0,0,n,maze,solution)
def mazeInput(n):
    maze = []
    for i in range(n):
        maze.append(list(map(int,input().split())))
    return maze
    
n = int(input())
maze = mazeInput(n)
#print(maze)
printPath(n,maze)