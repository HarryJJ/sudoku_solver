ROW_COL_VALUES = set(range(1, 10))
MAX_ITERATIONS = 100
PRINT = True

# TODO might not be the best way of doing this?
GRID_1 = [1, 2, 3]
GRID_2 = [4, 5, 6]
GRID_3 = [7, 8, 9]

GRID_MAP = {
    1: GRID_1,
    2: GRID_1,
    3: GRID_1,
    4: GRID_2,
    5: GRID_2,
    6: GRID_2,
    7: GRID_3,
    8: GRID_3,
    9: GRID_3
}


class SudokuSolver:
    def __init__(self, sudoku_grid, print=PRINT):
        self.problem = sudoku_grid.problem
        self.backtrack_problem = self.problem.copy()
        self.solution = sudoku_grid.solution

        self.null_locations = None
        self.last_null_locations = None

        self.iterations = 0
        self.backtrack = None

        self.print = print

    def solve(self):
        while self.iterations <= MAX_ITERATIONS:

            self.calc_null_locations()
            if self.null_locations == self.last_null_locations:
                self.backtrack = 0

            for row, col in self.null_locations:

                row_vals = self.get_row_values(row)
                col_vals = self.get_col_values(col)
                grid_vals = self.get_grid_values(row, col)
                # TODO persist possible values somewhere

                if (self.is_valid(row_vals) is False) or (
                        self.is_valid(col_vals) is False) or (
                        self.is_valid(grid_vals) is False):
                    self.problem = self.backtrack_problem
                    self.backtrack += 1
                    break

                poss_row_vals = ROW_COL_VALUES - set(row_vals)
                poss_col_vals = ROW_COL_VALUES - set(col_vals)
                poss_grid_values = ROW_COL_VALUES - set(grid_vals)

                all_possible_values = poss_row_vals.intersection(
                    poss_col_vals).intersection(poss_grid_values)

                if len(all_possible_values) == 1:
                    value = all_possible_values.pop()
                    self.problem.at[row, col] = value
                elif self.backtrack is not None:
                    if len(all_possible_values) == 2:
                        value = list(all_possible_values)[self.backtrack]
                        self.problem.at[row, col] = value

            if self.check_solution():
                break

            self.iterations += 1
            self.last_null_locations = self.null_locations

        # TODO add in profile speed as additional return
        if self.check_solution():
            if self.print:
                print('Solved!')
            return True
        else:
            if self.print:
                print(f'Could not solve. Cells remaining: {len(self.null_locations)}')
            return False

    def calc_null_locations(self):
        self.null_locations = self.problem.isnull().stack()[
            lambda x: x].index.tolist()

    def get_row_values(self, row):
        return self.problem.loc[row].copy().dropna().to_list()

    def get_col_values(self, col):
        return self.problem[col].copy().dropna().to_list()

    def get_grid_values(self, row, col):
        grid_values = self.problem.loc[
            GRID_MAP[row], GRID_MAP[col]].values.reshape(-1, ).tolist()
        return [x for x in grid_values if str(x) != 'nan']

    @staticmethod
    def is_valid(values):
        return len(values) == len(set(values))

    def check_solution(self):
        if len(self.null_locations) == 0:
            return self.solution.equals(self.problem.astype(int))
        else:
            return False
