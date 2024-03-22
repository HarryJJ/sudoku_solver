# Sudoku Solver

This project is a Python implementation of a Sudoku solver. It consists of three main files:

- `main.py`: The entry point of the program. It initializes a Sudoku grid, creates a solver instance, and attempts to solve the Sudoku puzzle.
- `sudoku_grid.py`: Contains the `SudokuGrid` class, responsible for generating the initial Sudoku grid and problem based on a specified fraction of null cells.
- `sudoku_solver.py`: Defines the `SudokuSolver` class, which implements the logic for solving the Sudoku puzzle using backtracking.

## Sudoku Grid Concept

A Sudoku grid is a 9x9 square divided into nine 3x3 subgrids. The objective of Sudoku is to fill in the grid so that each row, column, and 3x3 subgrid contains all of the digits from 1 to 9 without repetition. The puzzle starts with some cells already filled in, and the player must fill in the remaining cells following the rules of Sudoku.

## Usage

To use the Sudoku solver, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the cloned repository.
4. Run the `main.py` file using Python: `python main.py`.
5. The solver will attempt to solve the Sudoku puzzle and print the solution if successful.

## Customization

You can customize the behavior of the solver by modifying certain parameters:

- `FRAC_NULL` in `sudoku_grid.py`: Adjusts the fraction of null cells in the generated Sudoku problem.
- `MAX_ITERATIONS` in `sudoku_solver.py`: Sets the maximum number of iterations for the solver to attempt before giving up.
- `PRINT` in `sudoku_solver.py`: Controls whether debugging information is printed during the solving process.

## How the Sudoku Solver Works

The Sudoku solver utilizes a backtracking algorithm to fill in the Sudoku grid. Here's how it works:

1. The solver iterates through each empty cell (null cell) in the grid.
2. For each empty cell, it determines the possible values that can be placed in that cell based on the current state of the grid (row, column, and subgrid constraints).
3. If there's only one possible value for a cell, it fills in that value. Otherwise, it attempts another null cell. If there are two possible values it will attempt one and backtrack to the previous decision point if the chosen value is found to be incorrect at a later stage
4. The solver continues this process until either the puzzle is solved or it reaches the maximum number of iterations specified.

## Dependencies

This project has no external dependencies beyond the Python standard library.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
