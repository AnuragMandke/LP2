def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def is_safe(board, row, col, n):
    # Check this row and this column
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check diagonals
    for i in range(n):
        for j in range(n):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True


if __name__ == "__main__":
    n = int(input("Enter the board size (n): "))

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print("Solution exists:")
        print_solution(board, n)
    else:
        print("No solution exists.")