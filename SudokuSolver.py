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

def showBoard(sudokuBoard):
    for x in range(9):
        if x % 3 == 0 or x == 0:
            print(" - - -  - - -  - - -")
        for y in range(9):
            # if y==0 :
            #    print("|",end='')
            if y != 8:
                if y == 0 or y % 3 == 0:
                    #if it's the first number in the list
                    # add the line symbol
                    print("|",end='')
                # all lines expect the last should have
                # a space and continue in the same line
                print(str(sudokuBoard[x][y]) + " ", end='')
            else:
                # Last number in that line should print
                # the values with the line and proceed to the next line
                print(str(sudokuBoard[x][y]) + "|", end='\n')
    print(" - - -  - - -  - - -")

#Main code below
showBoard(board)
