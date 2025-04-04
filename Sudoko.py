class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.subgrid_size = 3

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row))
        print()

    def find_empty(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:  # 0 means the cell is empty
                    return r, c
        return None

    def is_valid(self, num, row, col):
        # Check row
        if num in self.board[row]:
            return False
        # Check column
        if num in [self.board[r][col] for r in range(self.size)]:
            return False
        # Check subgrid
        start_row, start_col = row - row % self.subgrid_size, col - col % self.subgrid_size
        for r in range(start_row, start_row + self.subgrid_size):
            for c in range(start_col, start_col + self.subgrid_size):
                if self.board[r][c] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Puzzle solved
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0  # Backtrack

        return False

    def csp_solve(self):
        if self.solve():
            return self.board
        return None

if __name__ == "__main__":
    # Initial Sudoku board (0 represents empty cells)
    initial_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    sudoku = Sudoku(initial_board)

    print("Initial Sudoku Board:")
    sudoku.print_board()
    
    solved_board = sudoku.csp_solve()

    if solved_board:
        print("Solved Sudoku Board:")
        sudoku.print_board()
    else:
        print("No solution exists.")