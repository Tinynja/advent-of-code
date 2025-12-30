# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = self.data.split('\n\n')
	
	def solve1(self):
		self.part1 = 0
		for g in self.data:
			for q in range(97,97+26):
				if chr(q) in g:
					self.part1 += 1

	def solve2(self):
		self.part2 = 0
		for g in self.data:
			n_peeps = g.count('\n')+1
			for q in range(97,97+26):
				if g.count(chr(q)) == n_peeps:
					self.part2 += 1