from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver

FRAC_NULL = .8
SIMULATIONS = 1000
PRINT = False


class TestSolver:
    def __init__(self, solver, frac_null, simulations=SIMULATIONS, print=PRINT):
        self.solver = solver
        self.frac_null = frac_null
        self.simulations = simulations
        self.results = []

        self.print = print

    def simulate(self):
        print(f'Running {self.simulations} simulations...')
        for simulation in range(0, self.simulations):
            sudoku = SudokuGrid(self.frac_null)
            solver = self.solver(sudoku, print=self.print)
            is_solved = solver.solve()
            self.results.append(is_solved)

        number_of_solved = [result for result in self.results if result is True]
        print(f'{len(number_of_solved)} out of {self.simulations} simulations were solved')


if __name__ == "__main__":
    test_solver = TestSolver(SudokuSolver, FRAC_NULL)
    test_solver.simulate()
