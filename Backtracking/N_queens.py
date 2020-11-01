placements = 0

def totalNQueens(n):
    board = [0] * n
    queenPlace(n, board, 0)
    return placements

def queenPlace(n, board, curRow):
    global placements
    # If place queens in all the rows, increment the # of placements.
    if curRow == n:
        placements += 1
        return
    # Recursively pick each column
    for col in range(n):
        board[curRow] = col
        # check if the board is valid
        if isValid(board, curRow, col):
            queenPlace(n, board, curRow + 1)
        # backtrack
        board[curRow] = 0

def isValid(board, curRow, curCol):
    for row in range(curRow):
        # If there are column or diagonal conflicts.
        if board[row] == curCol or abs(curRow - row) == abs(curCol - board[row]):
            return False
    return True

if __name__ == '__main__':
    n = 4
    print(totalNQueens(n))