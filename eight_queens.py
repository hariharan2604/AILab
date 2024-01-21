N = int(input("Enter the size of the Chess Board: "))


def solveNQueens(board, col):
    if col == N:
        # print(board)
        for row in board:
            for element in row:
                print(element, end=" ")
            print()
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True


board_init = [[0 for x in range(N)] for y in range(N)]
if not solveNQueens(board_init, 0):
    print("No solution found")
