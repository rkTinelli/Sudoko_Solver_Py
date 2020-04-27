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

def findEmpty(sudokuBoard):
    for x in range(9):
        for y in range(9):
            if sudokuBoard[x][y] == 0:
                return (x, y)
            # returns None if nothing was found


def checkIfValid(sudokuBoard, number, pos):
    # Check if the number tested is valid in the line
    for i in range(9):
        # keep the line fixed, change column, if equals to the number tested, is not valid
        if sudokuBoard[pos[0]][i] == number:
            #print("invalid in line") # Print for debug only
            return False

    # Check if the number tested is valid in the column
    for j in range(9):
        # keep the column fixed, change line, if equals to the number tested, is not valid
        if sudokuBoard[j][pos[1]] == number:
            #print("invalid in column") # Print for debug only
            return False

    # Identify subsquare
    subSquareX = pos[0] // 3
    subSquareY = pos[1] // 3
    '''Check if the number tested is valid in the subsquare
    For that the range needs to go from the initial position of the subsquare
    until that position + 3. E.G: pos(5,5) -> subSquare(1,1) -> range will go from 3 to 6
    testing positions (3,3) until (3,5)[Lines] (5,3)[Column]'''
    for i in range(subSquareX * 3, subSquareX * 3 + 3):
        for j in range(subSquareY * 3, subSquareY * 3 + 3):
            if sudokuBoard[i][j] == number:
                #print("invalid in square") # Print for debug only
                return False

    # Return true for valid values if it passed in all the checks above
    return True


def showBoard(sudokuBoard):
    for x in range(9):
        if x % 3 == 0 or x == 0:
            # if it's the first line or after a group for 3 lines with values, print the division
            print(" - - -  - - -  - - -")
        for y in range(9):
            if y != 8:  # going for every element of the line, expect the last one
                if y == 0 or y % 3 == 0:
                    # if it's the first number in the list, or after a group of 3 numbers, add the line symbol
                    print("|", end='')
                # all lines expect the last should have a space and continue in the same line
                print(str(sudokuBoard[x][y]) + " ", end='')
            else:
                # Last number in that line should print the values with the line and proceed to the next line
                print(str(sudokuBoard[x][y]) + "|", end='\n')
    print(" - - -  - - -  - - -")


# Main code below
showBoard(board)
