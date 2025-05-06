import sys

# Check if placing a queen at (row, col) is safe
def is_safe(board, row, col, n):
    # Check this row and this column
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check diagonals
    # Top-left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1
    # Bottom-left
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1; j -= 1
    # Top-right
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1; j += 1
    # Bottom-right
    i, j = row, col
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1; j += 1
    return True

# Backtracking solver for N-Queens
def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            # Backtrack
            board[row][col] = 0
    return False

# Print the board solution
def print_solution(board, n):
    for row in range(n):
        print(' '.join(str(cell) for cell in board[row]))

if __name__ == '__main__':
    try:
        n = int(input('Enter the board size (n): '))
    except ValueError:
        print('Invalid input. Please enter an integer.')
        sys.exit(1)
    # Initialize board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print('Solution exists:')
        print_solution(board, n)
    else:
        print('No solution exists')