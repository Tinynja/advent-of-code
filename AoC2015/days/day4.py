from day import Day
import hashlib

class Day4(Day):
	def __init__(self):
		super().__init__(__name__)
	
	def solve1(self):
		while True:
			self.part1 += 1
			if hashlib.md5((self.data + str(self.part1)).encode()).hexdigest()[0:5] == '00000':
				break
	
	def solve2(self):
		while True:
			self.part2 += 1
			if hashlib.md5((self.data + str(self.part2)).encode()).hexdigest()[0:6] == '000000':
				break