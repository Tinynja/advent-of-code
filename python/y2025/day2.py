# Builtin
import re
from math import ceil

# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.data = [list(map(int, d.split("-"))) for d in self.data.split(",")]

    def solve1(self):
        self.part1 = 0
        for _id in self.make_iterator():
            _id_str = str(_id)
            median = ceil(len(_id_str) / 2)
            if _id_str[0:median] == _id_str[median:]:
                self.part1 += _id
    
    def solve2(self):
        self.part2 = 0
        for _id in self.make_iterator():
            if re.fullmatch(r"(\d+)\1+", str(_id)):
                self.part2 += _id
    
    def make_iterator(self):
        return ( i for start,stop in self.data for i in range(start, stop+1) )