# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to check if a number can be placed in a specific position
def is_safe(grid, row, col, num):
    # Check if the number is in the same row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check if the number is in the same column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if the number is in the same 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(grid):
    empty_pos = find_empty(grid)
    if not empty_pos:
        return True  # Puzzle solved
    row, col = empty_pos

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Backtrack

    return False

# Function to find an empty space in the Sudoku grid
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # Return row, column of empty space
    return None

# Input Sudoku puzzle (0 represents empty spaces)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle and print the result
if solve_sudoku(sudoku_grid):
    print("Solved Sudoku grid:")
    print_grid(sudoku_grid)
else:
    print("No solution exists")
