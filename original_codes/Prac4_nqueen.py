# =====================================================================
# PRACTICAL 4: N-QUEENS PROBLEM (Using Backtracking)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Problem: N x N chessboard par N queens ko aise rakhna hai ki koi
#          ek doosre par attack na kare (Row, Col, ya Diagonal me).
# =====================================================================

# Board ko print karne ka helper function
def print_board(board, N):
    for row in range(N):
        for col in range(N):
            print("Q" if board[row][col] == 1 else ".", end=" ")
        print()
    print("-" * 20)

# Q2. CONSTRAINT / SAFETY CHECK: Kya is position (row, col) par Queen rakhna safe hai?
# Note: Hum left se right (column 0 se N-1) queens place karte hain,
# isliye hume sirf LEFT side check karni hoti hai (right me abhi tak koi queen nahi hai).
def is_safe(board, row, col, N):
    # Check 1: Kya same row me piche koi Queen hai?
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check 2: Upper-left diagonal check (\ direction)
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check 3: Lower-left diagonal check (/ direction)
    r, c = row + 1, col - 1
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True  # Agar teenon jagah koi attack nahi hai, to safe hai!

# Recursive Backtracking Function
def solve_nqueen(board, col, N):
    # Q3. GOAL CHECK: Kab rukna hai?
    # Agar col == N ho gaya, iska matlab saari N queens successfully baith chuki hain!
    if col == N:
        return True

    # Q4. EXPLORATION / TRY ALL OPTIONS: Current column me kis row par queen rakhein?
    # Row 0 se N-1 tak har row me rakh kar try karo:
    for row in range(N):
        # Pehle check karo safe hai ya nahi
        if is_safe(board, row, col, N):
            # 1. Action: Queen ko yahan place karo
            board[row][col] = 1

            # 2. Next Step: Agle column ke liye recursion chalao
            if solve_nqueen(board, col + 1, N):
                return True

            # 3. BACKTRACK: Agar aage solution nahi mila, to queen hata do (0 kar do)
            board[row][col] = 0

    # Agar kisi bhi row me place nahi ho paya, to piche backtrack karne ke liye False bhejo
    return False

# Driver Code
if __name__ == '__main__':
    val = input("Enter number of Queens (N, default 4): ").strip()
    N = int(val) if val else 4

    # Q1. STATE / ENVIRONMENT: Board kaisa dikhta hai?
    # N x N ka 2D list jisme sab jagah 0 (empty) hai.
    board = [[0] * N for _ in range(N)]

    if solve_nqueen(board, 0, N):
        print(f"\n{N}-Queens Solution Found:")
        print_board(board, N)
    else:
        print("Solution does not exist!")
