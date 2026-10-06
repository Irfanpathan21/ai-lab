# =====================================================================
# PRACTICAL 5: MINIMAX ALGORITHM (Tic-Tac-Toe Game)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Goal: Computer (AI / Maximizer 'X') kabhi nahi harega.
#       Human (Minimizer 'O') ke against best move choose karna.
# =====================================================================

# Q1. STATE / ENVIRONMENT: Board kaisa dikhta hai?
# 9 positions ka list, shuru me sab jagah ' ' (blank) hai. Index 0 se 8.
board = [' '] * 9

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# Q2. WIN / DRAW CHECK: Khel kaun jeeta ya draw hua?
def check_win(player):
    # Tic-tac-toe me sirf 8 winning patterns hote hain:
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 3 Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 3 Columns
        [0, 4, 8], [2, 4, 6]              # 2 Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def is_full():
    return ' ' not in board

# Q3. STOPPING / TERMINAL EVALUATION: Minimax me base condition kya hai?
# Bot jeeta to +1, Human jeeta to -1, Draw hua to 0.
def minimax(is_maximizing):
    if check_win('X'):
        return 1   # Bot jeet gaya (+1)
    if check_win('O'):
        return -1  # Human jeet gaya (-1)
    if is_full():
        return 0   # Match draw (0)

    # Q4. EXPLORATION / BEST MOVE SIMULATION:
    # Saari khali jagaho par move rakh ke check karo ki kisme best score milega.
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'             # Move chalo
                score = minimax(False)      # Opponent ka turn dekho
                board[i] = ' '             # Undo move
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'             # Move chalo
                score = minimax(True)       # Opponent ka turn dekho
                board[i] = ' '             # Undo move
                best_score = min(best_score, score)
        return best_score

# Bot ka move decide karne ka function
def bot_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'
    print(f"Bot ('X') chose position {move}")

# Driver Code: Game loop
print("Tic-Tac-Toe with Minimax AI (Bot = 'X', You = 'O')")
print("Positions are 0 to 8:\n 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")

while True:
    bot_move()
    print_board()
    if check_win('X'):
        print("Bot wins! (Minimax is unbeatable)")
        break
    if is_full():
        print("It's a Draw!")
        break

    # Player ka move
    p_move = int(input("Enter your move (0-8): "))
    while board[p_move] != ' ':
        p_move = int(input("Invalid position! Enter again (0-8): "))
    board[p_move] = 'O'
    print_board()

    if check_win('O'):
        print("Congratulations! You won!")
        break
    if is_full():
        print("It's a Draw!")
        break
