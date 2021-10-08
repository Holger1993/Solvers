import solver

def main():
    with open('Sudokus/sudoku1.txt') as f:
        lines = f.read().splitlines()
    f.close()
    sudoku = []
    for line in lines:
        lin = line.split(',')
        row = []
        for l in lin:
            row.append(int(l))
        sudoku.append(row)
    
    sudoku = solver.solve(sudoku)
    for row in sudoku:
        print(row)

if __name__ == "__main__":
    main()