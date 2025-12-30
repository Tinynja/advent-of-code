# Builtin
from math import floor

# Local
from ..solver import SolverABC


class Solver(SolverABC):
	def init(self):
		self.data = list(map(int, self.data.split()))
	
	def solve1(self):
		self.part1 = 0
		self.part2 = 0
		for mass in self.data:
			self.part1 += self.calc_fuel(mass)
			self.part2 += self.calc_fuel(mass, ignore_fuel_mass=False)
	
	def solve2(self):
		pass
	
	def calc_fuel(self, mass, ignore_fuel_mass=True):
		fuel = max(floor(mass/3)-2, 0)
		return (fuel+self.calc_fuel(fuel, ignore_fuel_mass=ignore_fuel_mass) if not ignore_fuel_mass and fuel else fuel)