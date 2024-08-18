def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col, solutions):
        if col >= n:
            solution = []
            for i in range(n):
                row = ''.join('Q' if board[i][j] == 1 else '.' for j in range(n))
                solution.append(row)
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, solutions)

    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

# Example usage
n = 8
all_solutions = solve_n_queens(n)
print(f"Found {len(all_solutions)} solutions for {n}-Queens problem:")
print_solutions(all_solutions)