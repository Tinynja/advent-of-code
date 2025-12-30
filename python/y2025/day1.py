# Builtin
from math import floor

# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.dial_init = 50
        self.dial_size = 100

        self.data = self.data.split("\n")
        self.data = [
            (1 if d[0] == "R" else -1) * int(d[1:])
            for d in self.data
            if int(d[1:]) != 0
        ]

    def solve1(self):
        dial = self.dial_init
        self.part1 = dial == 0
        for d in self.data:
            dial = (dial + d) % self.dial_size
            self.part1 += dial == 0
    
    def solve2(self):
        dial = self.dial_init
        self.part2 = dial == 0
        for d in self.data:
            # Method 1: O(n)
            dial_prev = dial
            dial += d
            self.part2 += (
                max(0, floor(dial/self.dial_size)) + 
                max(0, floor(-dial/self.dial_size)) + 
                (dial <= 0 and dial_prev != 0)
            )
            dial %= self.dial_size

            # Method 2: O(n^2)
            # movement = +1 if d > 0 else -1
            # for _ in range(abs(d)):
            #     dial = (dial + movement) % self.dial_size
            #     self.part2 += dial == 0