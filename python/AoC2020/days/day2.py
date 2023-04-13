from day import Day
import re

class Day2(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = self.data.split('\n')
		self.part1 = 0
		self.part2 = 0
	
	def solve1(self):
		for d in self.data:
			n1, n2, char, passwd = self.split_data(d)
			result_1 = len(re.findall(char, passwd))
			result_2 = (passwd[n1-1] == char) ^ (passwd[n2-1] == char)
			if result_1 >= n1 and result_1 <= n2:
				self.part1 += 1
			if result_2:
				self.part2 += 1
	
	def solve2(self):
		pass

	def split_data(self, line):
		line = line.split(' ')
		return list(map(int, line[0].split('-'))) + [line[1].replace(':',''), line[2]]
