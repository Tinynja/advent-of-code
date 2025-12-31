# Pypi
import numpy as np

# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.data = np.array([
            [cell == "@" for cell in row]
            for row in self.data.split("\n")
        ])

    def solve1(self):
        self.part1 = self.check_accessible(self.data).sum()
    
    def solve2(self):
        self.part2 = 0
        count = -1
        data = self.data.copy()
        while count != 0:
            accessible = self.check_accessible(data)
            count = accessible.sum()
            self.part2 += count
            data &= ~(accessible)
    
    def check_accessible(self, data):
        count = -data.astype(int)
        nrow, ncol = data.shape

        padded_data = np.zeros(np.array(data.shape) + 2, dtype=bool)
        padded_data[1:-1,1:-1] = data

        for dr in range(3):
            for dc in range(3):
                count += padded_data[dr:nrow+dr, dc:ncol+dc]

        return (count < 4) & data