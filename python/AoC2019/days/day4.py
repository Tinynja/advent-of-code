from day import Day

class Day4(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = list(map(int, self.data.split('-')))
	
	def solve1(self):
		for i in range(self.data[0], self.data[1]+1):
	
	def next_asc_passwd(current_passwd):
		digit_to_increment = len(current_passwd)-1
		for i in range(1,len(current_passwd)):
			if current_passwd[i] < current_passwd[i-1]:
				
