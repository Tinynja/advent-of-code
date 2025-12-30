# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.wire1, self.wire2 = [[d for d in w.split(',')] for w in self.data.split('\n')]

	def solve1(self):
		path1, _ = self.generate_path(self.wire1)
		print(len(path1))
		path2, intersections = self.generate_path(self.wire2, compare_path=path1)
		print(len(path2))
		self.part1 = None
		for i in intersections:
			if self.part1 is None or abs(i[0])+abs(i[1]) < self.part1:
				self.part1 = abs(i[0])+abs(i[1])
	
	def solve2(self):
		...

	def generate_path(self, directions, compare_path=None):
		x,y,path,intersections = 0,0,[],[]
		for d in directions:
			for i in range(int(d[1:])):
				x += {'R':1, 'D':0, 'L':-1, 'U':0}[d[0]]
				y += {'R':0, 'D':-1, 'L':0, 'U':1}[d[0]]
				path.append([x,y])
				if compare_path is not None and [x,y] in compare_path:
					intersections.append([x,y])
		return path, intersections

	def check_intersection(self, line1, line2):
		# Orientation is 1 if horizontal (y1 == y2)
		orient1 = line1[0][1] == line1[1][1]
		orient2 = line2[0][1] == line2[1][1]
		if orient1 == orient2:
			pass
		else:
			pass