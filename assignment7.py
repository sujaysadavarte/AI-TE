"""B3: Backtracking search for the 8-Queens CSP."""
 
 
def is_safe(board, row, col):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True
 
 
def solve_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1, n):
                return True
            board[row] = -1  # backtrack
    return False
 
 
def count_solutions(board, row, n):
    if row == n:
        return 1
    total = 0
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            total += count_solutions(board, row + 1, n)
            board[row] = -1
    return total
 
 
def print_board(board, n):
    for row in range(n):
        print(" ".join("Q" if board[row] == col else "." for col in range(n)))
 
 
if __name__ == "__main__":
    n = 8
    board = [-1] * n
    if solve_queens(board, 0, n):
        print("Solution for 8-Queens Problem:\n")
        print_board(board, n)
        print("\nColumn of queen in each row:", board)
    else:
        print("No solution exists.")
    print("Total number of solutions for n = 8:",
          count_solutions([-1] * n, 0, n))
