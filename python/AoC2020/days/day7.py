from day import Day
import re

class Day7(Day):
	def __init__(self):
		super().__init__(__name__)
		self.data = self.data.split('\n')
		self.rules = {}
		self.read_rules()
	
	def solve1(self):
		for b in self.rules:
			if b != 'shiny gold' and self.search_bag(b, 'shiny gold'):
				self.part1 += 1
	
	def solve2(self):
		self.part2 = self.count_bags('shiny gold')-1

	def read_rules(self):
		for r in self.data:
			bag_type = re.match(r'([a-z ]+) bags contain', r).group(1)
			bag_contents = {g[1]:int(g[0]) for g in re.findall(r'(\d+) ([a-z ]+) bags?', r)}
			self.rules[bag_type] = bag_contents

	def search_bag(self, container_bag, bag_to_search):
		for b in self.rules[container_bag]:
			if b == bag_to_search or self.search_bag(b, bag_to_search):
				return True
		return False
	
	def count_bags(self, container_bag):
		n_bags = 1
		for b,n in self.rules[container_bag].items():
			n_bags += n*self.count_bags(b)
		return n_bags
