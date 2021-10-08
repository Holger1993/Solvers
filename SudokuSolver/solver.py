def fixIt(sudoku):
    find = findSpot(sudoku)
    if not find:
        return True
    i, j = find
    for val in range(1,10):
        if is_poss(val, sudoku, i, j):
            sudoku[i][j] = val
            if fixIt(sudoku):
                return True
            sudoku[i][j] = 0
    return False


def findSpot(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return (row, col)
    return False

def is_poss(val, sudoku, i, j):
    for col in range(9):
        if sudoku[i][col] == val and col != j:
            return False
    for row in range(9):
        if sudoku[row][j] == val and row != i:
            return False

    box_x = j // 3
    box_y = i // 3

    for col in range(box_y * 3, box_y * 3 + 3):
        for row in range(box_x * 3, box_x * 3 + 3):
            if sudoku[col][row] == val and (col, row) != (i, j):
                return False

    return True

def solve(sudoku):
    fixIt(sudoku)
    return sudoku