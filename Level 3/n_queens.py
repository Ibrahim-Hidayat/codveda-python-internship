def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


def main():
    try:
        n = int(input("Enter N (the board size): "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return
    if n < 1:
        print("Error: N must be at least 1.")
        return
    board = [[0] * n for _ in range(n)]
    if solve(board, 0, n):
        print(f"\nSolution for N = {n}:\n")
        print_board(board)
    else:
        print(f"No solution exists for N = {n}.")


if __name__ == "__main__":
    main()