from day import Day
from copy import deepcopy
import re

class Day8(Day):
	def __init__(self):
		super().__init__(__name__)
		data = self.data
		self.data = []
		for d in data.splitlines():
			match = re.match(r'(.*) ((?:\+|-)\d+)', d)
			self.data.append({'inst':match.group(1), 'arg':int(match.group(2))})
	
	def solve1(self):
		_, acc = self.exec_code(self.data)
		self.part1 = acc
	
	def solve2(self):
		for addr in range(len(self.data)):
			if self.data[addr]['inst'] in ('nop', 'jmp'):
				# Copy original data so that we can modify instructions
				code = deepcopy(self.data)
				# Swap instructions
				code[addr]['inst'] = ('nop', 'jmp')[code[addr]['inst'] == 'nop']
				exit_status, acc = self.exec_code(code, copy_code=False)
				if exit_status == 0:
					self.part2 = acc
					break
	
	def exec_code(self, code, copy_code=True):
		# Copy the code so that we can add the "executed" key without messing with the original data
		if copy_code: code = deepcopy(code)
		acc, addr = 0, 0
		while addr < len(code) and 'executed' not in code[addr]:
			code[addr]['executed'] = True
			acc, addr = self.exec_instruction(code[addr]['inst'], code[addr]['arg'], acc, addr)
		if addr == len(code):
			return 0, acc
		else:
			return 1, acc

	def exec_instruction(self, inst, arg, acc, addr):
		if inst == 'acc':
			acc += arg
			addr += 1
		elif inst == 'jmp':
			addr += arg
		elif inst == 'nop':
			addr += 1
		return acc, addr
