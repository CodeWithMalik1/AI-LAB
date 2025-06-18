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