# Builtin
import inspect
from pathlib import Path
from abc import ABC, abstractmethod


class SolverABC(ABC):
	def __init__(self):
		self.part1 = None
		self.part2 = None

		self.src_path = Path(inspect.getfile(self.__class__))
		self.input_path = self.src_path.with_suffix('.txt')

		with open(self.input_path) as f:
			self.data = f.read()
		
		self.init()
	
	def init(self):
		...

	@abstractmethod
	def solve1(self):
		self.part1 = ...
	
	@abstractmethod
	def solve2(self):
		self.part2 = ...