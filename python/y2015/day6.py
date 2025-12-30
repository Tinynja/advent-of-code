# Builtin
import re

# Pypi
import numpy as np

# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		interpreted_data = []
		for line in self.data.split('\n'):
			if line.startswith('turn off'):
				action = 0
			elif line.startswith('turn on'):
				action = 1
			elif line.startswith('toggle'):
				action = 2
			line = re.sub(r'(turn on|turn off|toggle|through) ', '', line)
			instruction = dict(zip(['x0', 'y0', 'x1', 'y1'], list(map(int, re.split(r'[, ]', line)))))
			instruction['action'] = action
			interpreted_data.append(instruction)
		self.data = interpreted_data
	
	def solve1(self):
		gridlight = np.zeros((1000,1000))
		for inst in self.data:
			if inst['action'] == 2:
				gridlight[inst['x0']:inst['x1']+1, inst['y0']:inst['y1']+1] = np.logical_not(gridlight[inst['x0']:inst['x1']+1, inst['y0']:inst['y1']+1])
			else:
				gridlight[inst['x0']:inst['x1']+1, inst['y0']:inst['y1']+1] = inst['action']
		self.part1 = np.count_nonzero(gridlight == 1)

	def solve2(self):
		gridlight = np.zeros((1000,1000))
		min_0 = np.vectorize(lambda x: max(x, 0))
		for inst in self.data:
			gridlight[inst['x0']:inst['x1']+1, inst['y0']:inst['y1']+1] = min_0(gridlight[inst['x0']:inst['x1']+1, inst['y0']:inst['y1']+1] + [-1, 1, 2][inst['action']])
		self.part2 = int(np.sum(gridlight))