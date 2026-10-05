# =====================================================================
# PRACTICAL 5: MINIMAX ALGORITHM (Tic-Tac-Toe AI)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Game Playing / Adversarial Search
# CORE CONCEPT:
#   AI ('X') is Maximizer -> seeks maximum score (+1).
#   Human ('O') is Minimizer -> seeks minimum score (-1).
#   Draw -> score is 0.
#   Recursively evaluate all future outcomes and choose optimal branch.
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Alpha-Beta Pruning: Just add alpha and beta bounds to minimax()!
#   - Any 2-Player Zero-Sum Game (Nim, Connect-4):
#     Replace win conditions and board representation; minimax loop is IDENTICAL.
# =====================================================================

# 1. State / Board Representation (9 cells: 0 to 8)
board = [' '] * 9

# All 8 Winning Combinations (3 rows, 3 cols, 2 diagonals)
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_win(player):
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def print_board():
    for i in (0, 3, 6):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
    print()

# 2. Universal Minimax Template Function
def minimax(is_max):
    if check_win('X'): return 1
    if check_win('O'): return -1
    if ' ' not in board: return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_score, move = -999, -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score, move = score, i
    return move

# 3. Demonstration / Driver Code
# Setup a scenario where Human ('O') threatens to win, AI ('X') must block/win
print("Tic-Tac-Toe Minimax Demonstration:")
board[0] = 'X'
board[1] = 'O'
board[4] = 'O'
print("Current Board:")
print_board()

ai_pos = best_move()
print(f"AI calculates optimal move: Position {ai_pos}")
board[ai_pos] = 'X'
print("\nBoard after AI Move:")
print_board()
