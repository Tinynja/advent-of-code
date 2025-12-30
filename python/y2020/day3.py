# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = [[x for x in l] for l in self.data.split('\n')]
	
	def solve1(self):
		self.part1 = 0
		self.part1 = self.slope_run(3,1)
	
	def solve2(self):
		self.part2 = 1
		slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
		for s in slopes:
			self.part2 *= self.slope_run(s[0], s[1])

	def slope_run(self, dx, dy):
		x,y,trees = 0,0,0
		while y+dy < len(self.data):
			x += dx
			y += dy
			if self.data[y][x%len(self.data[0])] == '#':
				trees += 1
		return trees
