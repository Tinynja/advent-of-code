from day import Day

class Day2(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = [list(map(int, b.split('x'))) for b in self.data.split()]
	
	def solve1(self):
		for l,w,h in self.data:
			self.part1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
			self.part2 += min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h
	
	def solve2(self):
		pass
