from day import Day
import re

class Day6(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = self.data.split('\n\n')
	
	def solve1(self):
		for g in self.data:
			for q in range(97,97+26):
				if chr(q) in g:
					self.part1 += 1

	def solve2(self):
		for g in self.data:
			n_peeps = g.count('\n')+1
			for q in range(97,97+26):
				if g.count(chr(q)) == n_peeps:
					self.part2 += 1