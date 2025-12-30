# Pypi
import numpy as np

# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = np.array(list(map(int, self.data.split())))
		self.data.sort()

	def solve1(self):
		for x in self.data:
			if x in 2020-self.data:
				self.part1 = x*(2020-x)
				break

	def solve2(self):
		data_filt = self.data[self.data <= (2020-self.data[0]-self.data[1])]

		for i,x in enumerate(data_filt):
			for j,y in enumerate(data_filt):
				if 2020-x-y in data_filt and i != j:
					self.part2 = x*y*(2020-x-y)
					return