from day import Day

class Day5(Day):
	def __init__(self):
		super().__init__(__name__)
		self.interpret_data()
	
	def solve1(self):
		self.part1 = max(self.data['seatid'])
	
	def solve2(self):
		for row in range(min(self.data['row'])+1, max(self.data['row'])):
			for col in range(0,8):
				seatid = (row<<3)+col
				if seatid not in self.data['seatid'] and seatid+1 in self.data['seatid'] and seatid-1 in self.data['seatid']:
					self.part2 = seatid
					break
	
	def interpret_data(self):
		self.data = {'raw': self.data.split(), 'col':[], 'row':[], 'seatid':[]}
		for s in self.data['raw']:
			row = int(s[0:7].translate(str.maketrans('BF', '10')), 2)
			col = int(s[7:10].translate(str.maketrans('RL', '10')), 2)
			seatid = (row<<3)+col
			self.data['row'].append(row)
			self.data['col'].append(col)
			self.data['seatid'].append(seatid)
