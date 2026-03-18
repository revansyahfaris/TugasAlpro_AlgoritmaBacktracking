import time

def print_board(board):
    """Helper function to visualize the board."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Finds an empty cell (marked as 0)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Checks if a number is valid based on Sudoku constraints."""
    # Check row [cite: 57]
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column [cite: 58]
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 quadrant [cite: 56]
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(board):
    """Core backtracking logic [cite: 60-64]."""
    find = find_empty(board)
    if not find:
        return True  # Solution found! [cite: 54]
    else:
        row, col = find

    for i in range(1, 10): # Try numbers 1-9 [cite: 53]
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            
            # Visualization of the step 
            print(f"\nTrying {i} at ({row}, {col}):")
            print_board(board)
            time.sleep(0.05) # Slow down for visibility

            if solve(board):
                return True

            # Backtracking step [cite: 63]
            board[row][col] = 0
            print(f"\nBacktracking from ({row}, {col})...")

    return False

# Initial board from Slide 10 [cite: 66-70]
puzzle = [
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
]

print("Starting Sudoku Solver...")
solve(puzzle)
print("\nFinal Solution Found:")
print_board(puzzle)