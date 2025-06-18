N = 8

# ✅ Function to print the board configuration
def printSolution(board):
    """
    Print the current chessboard configuration.
    'Q' indicates a queen, '.' indicates an empty space.
    """
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")
    

# ✅ Function to check if placing a queen is safe
def isSafe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col].
    It checks the column, upper-left, and upper-right diagonals.
    """
    # Check column above
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


# ✅ Recursive backtracking function to solve N-Queens
def solveNQueens(board, row, n):
    """
    Try to place queens row by row using backtracking.
    If a solution is found, print it.
    """
    if row == n:
        printSolution(board)
        return True

    result = False
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1  # Place queen
            result = solveNQueens(board, row + 1, n) or result
            board[row][col] = 0  # Backtrack

    return result


# ✅ Driver function
def nQueens(n):
    """
    Initialize the board and trigger the solver function.
    """
    board = [[0] * n for _ in range(n)]
    if not solveNQueens(board, 0, n):
        print("No solution exists.")
    else:
        print("Solutions printed above.")


# ✅ Main call to solve the N-Queens problem for N = 8
nQueens(N)
