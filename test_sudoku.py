import sudoku_solver

# test puzzle (0 represents empty cells)
board = [
    [3,4,5,0,0,0,0,0,0],
    [0,0,6,0,0,1,0,0,0],
    [8,0,1,0,7,0,2,0,0],
    [0,0,3,0,0,8,0,0,0],
    [6,0,0,0,0,0,0,5,0],
    [0,0,4,1,9,0,6,0,0],
    [0,0,0,6,0,5,1,0,3],
    [0,0,0,0,0,0,7,0,0],
    [0,0,0,0,0,4,0,0,0]
]

# solve the puzzle
sudoku_solver.solveSudoku(board)

# Print the solution
print("Solved Sudoku:")
for row in board:
    print(row)