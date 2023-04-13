from day import Day
import re

class Day5(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = self.data.split('\n')
	
	def solve1(self):
		for s in self.data:
			if any([n in s for n in ['ab', 'cd', 'pq', 'xy']]):
				continue
			elif re.search(r'([a-z])\1', s) and re.search(r'(a|e|i|o|u).*(a|e|i|o|u).*(a|e|i|o|u)', s):
				self.part1 += 1

	def solve2(self):
		for s in self.data:
			if re.search(r'([a-z]{2}).*\1', s) and re.search(r'([a-z]).\1', s):
				self.part2 += 1