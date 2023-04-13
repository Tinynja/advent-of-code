from day import Day
from copy import deepcopy

class Day2(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = list(map(int, self.data.split(',')))
	
	def solve1(self):
		self.part1 = self.computer(self.data, noun=12, verb=2)[0]
	
	def solve2(self):
		found = False
		for noun in range(100):
			for verb in range(100):
				if self.computer(self.data, noun=noun, verb=verb)[0] == 19690720:
					found = True
					self.part2 = 100*noun+verb
				if found: break
			if found: break
		
	def computer(self, src_intcode, noun=None, verb=None):
		intcode = deepcopy(src_intcode)
		intcode[1] = noun or intcode[1]
		intcode[2] = verb or intcode[2]
		opcode, pos = 0, -4
		while opcode != 99:
			pos += 4
			opcode = intcode[pos]
			if opcode == 1:
				intcode[intcode[pos+3]] = intcode[intcode[pos+1]]+intcode[intcode[pos+2]]
			elif opcode == 2:
				intcode[intcode[pos+3]] = intcode[intcode[pos+1]]*intcode[intcode[pos+2]]
			elif opcode != 99:
				print('Invalid opcode: ', opcode)
				break
		return intcode