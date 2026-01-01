# Builtin
import re

# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.data = self.data.split("\n")
            
        self.operator = re.findall("\+|\*", self.data.pop())
        
        self.terms1 = [list(map(int, re.findall("\d+", row))) for row in self.data]
        self.terms1 = tuple(zip(*self.terms1))
        
        self.terms2 = [list(row) for row in self.data]
        self.terms2 = tuple(zip(*self.terms2))
        self.terms2 = ["".join(term) for term in self.terms2]
        
        empty = " "*len(self.data)
        i = 0
        start = 0
        for end,term in enumerate(self.terms2):
            if term == empty:
                self.terms2[i] = list(map(int, self.terms2[start:end]))
                i += 1
                start = end+1
            elif end == len(self.terms2)-1:
                self.terms2[i] = list(map(int, self.terms2[start:end+1]))
        self.terms2 = self.terms2[:len(self.operator)]

    def solve1(self):
        self.part1 = 0
        for i,op in enumerate(self.operator):
            self.part1 += self.calculate(op, self.terms1[i])
    
    def solve2(self):
        self.part2 = 0
        for i,op in enumerate(self.operator):
            self.part2 += self.calculate(op, self.terms2[i])
    
    def calculate(self, operator, terms):
        if operator == "+":
            acc = 0
            fn = int.__add__
        elif operator == "*":
            acc = 1
            fn = int.__mul__
        for term in terms:
            acc = fn(acc, term)
        return acc
        