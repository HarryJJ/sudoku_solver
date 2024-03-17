from random import sample

import numpy as np
import pandas as pd

ROW_COLUMN_NAMES = list(range(1, 10))

BASE = 3
BASE_RANGE = range(BASE)
SIDE = BASE * BASE
FRAC_NULL = .6


class SudokuGrid:
    def __init__(self, frac_null=FRAC_NULL):
        self.frac_null = frac_null
        self.rows = self.generate_row()
        self.cols = self.generate_row()
        self.solution = pd.DataFrame(
            data=self.generate_grid(self.cols, self.rows),
            columns=ROW_COLUMN_NAMES,
            index=ROW_COLUMN_NAMES
        )
        self.problem = self.generate_problem()

    @staticmethod
    def shuffle_range(s):
        return sample(s, len(s))

    @staticmethod
    def pattern(r, c):
        return (BASE * (r % BASE) + r // BASE + c) % SIDE

    def generate_row(self):
        return [g * BASE + r for g in self.shuffle_range(BASE_RANGE) for r in
                self.shuffle_range(BASE_RANGE)]

    def generate_numbers(self):
        return self.shuffle_range(range(1, BASE * BASE + 1))

    def generate_grid(self, cols, rows):
        numbers = self.generate_numbers()
        return [[numbers[self.pattern(r, c)] for c in cols] for r in rows]

    def generate_problem(self):
        num_cells_to_null = int(
            self.solution.shape[0] * self.solution.shape[1] * self.frac_null
        )
        idx = np.random.choice(
            range(self.solution.shape[0]),
            int(num_cells_to_null)
        )
        cols = np.random.choice(range(self.solution.shape[1]), size=len(idx))

        problem = self.solution.copy().astype(object).to_numpy()
        problem[idx, cols] = [np.NAN] * num_cells_to_null

        return pd.DataFrame(
            problem,
            index=self.solution.index,
            columns=self.solution.columns
        )