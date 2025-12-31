# Local
from ..solver import SolverABC


class Solver(SolverABC):
    def init(self):
        self.fresh, self.available = self.data.split("\n\n")
        
        self.available = set(map(int, self.available.split("\n")))
        
        self.fresh = [list(map(int, fresh.split("-"))) for fresh in self.fresh.split("\n")]
        
        # Remove overlaps
        a_i = 0
        while a_i < len(self.fresh):
            a = self.fresh[a_i]
            b_i = a_i+1
            while b_i < len(self.fresh):
                b = self.fresh[b_i]
                if a[0] >= b[0] and a[1] <= b[1]:
                    # a is fully contained inside b
                    self.fresh.pop(a_i)
                    break
                elif b[0] >= a[0] and b[1] <= a[1]:
                    # b is fully contained inside a
                    self.fresh.pop(b_i)
                elif a[0] < b[0] and a[1] >= b[0]:
                    # a is lower than b but overlaps
                    a[1] = b[0] - 1
                    b_i += 1
                elif a[0] <= b[1] and a[1] > b[1]:
                    # a is higher than b but overlaps
                    a[0] = b[1] + 1
                    b_i += 1
                else:
                    b_i += 1
            else:
                a_i += 1

    def solve1(self):
        self.part1 = 0
        for ingredient in self.available:
            self.part1 += self.check_fresh(ingredient)
    
    def solve2(self):
        self.part2 = 0
        for f in self.fresh:
            self.part2 += f[1] - f[0] + 1
       
    def check_fresh(self, ingredient):
        for bounds in self.fresh:
            if bounds[0] <= ingredient <= bounds[1]:
                return True
            else:
                continue
        return False