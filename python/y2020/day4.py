# Builtin
import re

# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = [{d.split(':')[0]:d.split(':')[1] for d in passwd.split()} for passwd in self.data.split('\n\n')]
		self.required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	
	def solve1(self):
		self.part1 = 0
		for p in self.data:
			if all([req_f in list(p) for req_f in self.required_fields]):
				self.part1 += 1

	def solve2(self):
		self.part2 = 0
		for p in self.data:
			self.part2 += 1
			for req_f in self.required_fields:
				if req_f not in list(p):
					self.part2 -= 1
					break
				elif req_f == 'byr' and (int(p[req_f]) < 1920 or int(p[req_f]) > 2002):
					self.part2 -= 1
					break
				elif req_f == 'iyr' and (int(p[req_f]) < 2010 or int(p[req_f]) > 2020):
					self.part2 -= 1
					break
				elif req_f == 'eyr' and (int(p[req_f]) < 2020 or int(p[req_f]) > 2030):
					self.part2 -= 1
					break
				elif req_f == 'hgt' and (not re.fullmatch(r'[0-9]+(cm|in)', p[req_f]) or (
											not ('cm' in p[req_f] and int(p[req_f].replace('cm','')) >= 150 and int(p[req_f].replace('cm','')) <= 193)
											and not ('in' in p[req_f] and int(p[req_f].replace('in','')) >= 59 and int(p[req_f].replace('in','')) <= 76))):
					self.part2 -= 1
					break
				elif req_f == 'hcl' and not re.fullmatch(r'\#[0-9a-f]{6}', p[req_f]):
					self.part2 -= 1
					break
				elif req_f == 'ecl' and p[req_f] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
					self.part2 -= 1
					break
				elif req_f == 'pid' and not re.fullmatch(r'[0-9]{9}', p[req_f]):
					self.part2 -= 1
					break

			