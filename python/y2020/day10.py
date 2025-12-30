# Builtin
# from copy import deepcopy

# Pypi
import numpy as np

# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = list(map(int, self.data.splitlines()))
		self.data.sort()
	
	def solve1(self):
		data = np.array([0,] + self.data)
		self.part1 = np.count_nonzero(np.diff(data)==1) * (1+np.count_nonzero(np.diff(data)==3))
		# n_diff_1, n_diff_3 = 0, 1
		# data = deepcopy(self.data)
		# last_jolt = 0
		# for a in self.data:
		# 	if min(data) - last_jolt == 1:
		# 		n_diff_1 += 1
		# 	if min(data) - last_jolt == 3:
		# 		n_diff_3 += 1
		# 	last_jolt = min(data)
		# 	data.pop(data.index(min(data)))
		# self.part1 = n_diff_1*n_diff_3
	
	def solve2(self):
		pass
		# self.part2 = 1
		# data = np.diff(np.array([0, *self.data, max(self.data)+3]))
		# print(data)
		# for i in range(len(data)):
		# 	multiplier = 1
		# 	if i > 1 and data[i-1]:

		# 	i += 1