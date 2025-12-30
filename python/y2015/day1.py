# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def solve1(self):
		for inst in self.data:
			if inst == '(':
				self.part1 += 1
			else:
				self.part1 -= 1
	
	def solve2(self):
		for i,inst in enumerate(self.data):
			if inst == '(':
				self.part2 += 1
			else:
				self.part2 -= 1
			if self.part2 == -1:
				self.part2 = i+1
				break