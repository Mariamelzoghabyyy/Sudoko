🧠 Sudoku Solver in Python (Backtracking + CSP)

This project is a fully functional Sudoku solver built in Python. It uses a backtracking algorithm inspired by constraint satisfaction problem (CSP) strategies to solve any standard 9x9 Sudoku puzzle. The program reads a partially filled board, finds valid solutions recursively, and prints the completed board.

🎯 Features

Backtracking Algorithm: Uses a recursive backtracking search to try valid numbers in empty cells, reverting (backtracking) when a dead end is reached.

Constraint Checking: Ensures numbers are valid in their row, column, and 3x3 subgrid before placing them, following standard Sudoku rules.

Modular OOP Design: Encapsulated in a Sudoku class with methods for validation, printing, solving, and CSP integration.

Readable Console Output: Prints the Sudoku board before and after solving for easy comparison and debugging.

🧩 How It Works

The solver scans the grid for the first empty cell.

It tries digits from 1 to 9 in that cell.

If the digit is valid (no conflicts in row, column, or box), it proceeds recursively.

If stuck, it backtracks and tries a different number.

The algorithm continues until the board is completely filled or determines there's no solution.

📈 Future Enhancements

GUI Interface using Tkinter or PyGame.

Puzzle Generator to create random Sudoku puzzles with varying difficulty levels.

Performance Optimizations via heuristics (e.g., Most Constrained Variable or Forward Checking).
