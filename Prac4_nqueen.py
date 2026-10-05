# =====================================================================
# PRACTICAL 4: N-QUEENS PROBLEM (Backtracking)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Recursive Backtracking (Choose -> Recurse -> Backtrack)
# CORE CONCEPT:
#   Place queens column by column (0 to N-1).
#   For each column, test every row:
#     1. If safe: place Queen (board[row][col] = 1).
#     2. Recurse to next column: solve(col + 1).
#     3. If no solution ahead: remove Queen (board[row][col] = 0) and backtrack.
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Change Board Size: Change N = 4 to N = 8 (for 8-Queens problem).
#   - Any Backtracking Problem (Sudoku, Graph Coloring, Knight's Tour):
#     The 3-step structure is ALWAYS:
#       `make_move() -> if solve(next): return True -> undo_move()`
# =====================================================================

N = 4
board = [[0] * N for _ in range(N)]

# 1. Safety Check: Only check left side (since right side is empty so far)
def is_safe(row, col):
    # Check row on left
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper-left diagonal (\ direction)
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower-left diagonal (/ direction)
    r, c = row + 1, col - 1
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True

# 2. Universal Backtracking Template Function
def solve_nqueens(col=0):
    # Base Condition: All N queens are placed successfully!
    if col == N:
        return True

    for row in range(N):
        if is_safe(row, col):
            board[row][col] = 1              # Step 1: Choose (Place Queen)
            if solve_nqueens(col + 1):       # Step 2: Explore (Recurse next column)
                return True
            board[row][col] = 0              # Step 3: Un-choose (Backtrack)

    return False

# 3. Driver Code
print(f"--- {N}-Queens Solution ---")
if solve_nqueens(0):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
else:
    print("No solution exists!")
