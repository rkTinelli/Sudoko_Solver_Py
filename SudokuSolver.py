board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def printBoard(sudokuBoard):
    for x in range(9):
        for y in range(9):
            if y != 8:
                # all lines expect the last should have
                # a space and continue in the same line
                print(str(sudokuBoard[x][y]) + " ",end='')
            else:
                #Last number in that line should print
                #and proceed to the next line
                print(str(sudokuBoard[x][y]), end='\n')


printBoard(board)