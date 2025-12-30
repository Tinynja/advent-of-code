# Pypi
import numpy as np

# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.data = [[int(d) for d in bank] for bank in self.data.split("\n")]

    def solve1(self):
        self.part1 = 0
        for bank in self.data:
            self.part1 += self.find_largest_combination(bank, 2)
    
    def solve2(self):
        self.part2 = 0
        for bank in self.data:
            self.part2 += self.find_largest_combination(bank, 12)
    
    def find_largest_combination(self, digits, count):
        nb_digits = len(digits)
        found = []
        start = 0
        for end in range(nb_digits-count+1, nb_digits+1):
            start += np.argmax(digits[start:end]) + 1
            found.append(digits[start - 1])
        return int("".join(map(str,found)))