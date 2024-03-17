from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver


if __name__ == "__main__":
    new_sudoku = SudokuGrid()
    new_solver = SudokuSolver(new_sudoku)
    new_solver.solve()
