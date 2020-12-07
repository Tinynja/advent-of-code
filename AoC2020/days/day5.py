from day import Day

class Day5(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = self.data.split()
	
	def solve1(self):
		self.seat_rows = []
		for seat in self.data:
			row, _, seatid = self.calc_seatid(seat)
			self.part1 = max(self.part1, seatid)
			self.seat_rows.append(row)
	
	def solve2(self):
		for row in self.seat_rows:
			if row >= 2 and row-1 not in self.data:
				print(row)
				_, _, self.part2 = self.calc_seatid(self.data[self.seat_rows.index(row-1)])
				break
			elif row <= 125 and row+1 not in self.data:
				print(row)
				_, _, self.part2 = self.calc_seatid(self.data[self.seat_rows.index(row+1)])
				break
	
	def calc_seatid(seld, seat_txt):
		row = int(seat_txt[0:7].translate(str.maketrans('BF', '10')), 2)
		col = int(seat_txt[7:10].translate(str.maketrans('RL', '10')), 2)
		seatid = row*8+col
		return row, col, seatid
