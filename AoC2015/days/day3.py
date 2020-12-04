from day import Day

class Day3(Day):
	def __init__(self):
		super().__init__(__name__)
	
	def solve1(self):
		x,y = 0,0
		houses = [[0,0]]
		for d in self.data:
			x += {'>':1, 'v':0, '<':-1, '^':0}[d]
			y += {'>':0, 'v':-1, '<':0, '^':1}[d]
			if [x,y] not in houses: houses.append([x,y])
		self.part1 = len(houses)
	
	def solve2(self):
		x1,y1,x2,y2 = 0,0,0,0
		houses = [[0,0]]
		for i,d in enumerate(self.data):
			if i%2:
				x1 += {'>':1, 'v':0, '<':-1, '^':0}[d]
				y1 += {'>':0, 'v':-1, '<':0, '^':1}[d]
				if [x1,y1] not in houses: houses.append([x1,y1])
			else:
				x2 += {'>':1, 'v':0, '<':-1, '^':0}[d]
				y2 += {'>':0, 'v':-1, '<':0, '^':1}[d]
				if [x2,y2] not in houses: houses.append([x2,y2])
		self.part2 = len(houses)
