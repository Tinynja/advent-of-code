import os

class Day:
	def __init__(self, child_name):
		child_name = child_name.split('.')
		input_path = os.path.join(os.path.dirname(__file__), child_name[0], 'inputs', child_name[2] + '.txt')
		if os.path.isfile(input_path):
			with open(input_path) as f:
				self.data = f.read()
		else:
			print(f'Missing file {os.path.join(child_name[0], "inputs", child_name[2])}.txt')

	def solve1(self):
		raise NotImplementedError
	
	def solve2(self):
		raise NotImplementedError