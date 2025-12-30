# Builtin
import sys
import importlib
import re
from pathlib import Path

from traceback import format_exc

def get_years():
	years = {}
	for child in Path(__file__).parent.iterdir():
		if not child.is_dir():
			continue
		match = re.fullmatch(r'y([0-9]+)', child.name, flags=re.IGNORECASE)
		if match is None:
			continue
		years[int(match.group(1))] = child
	return years
	
def get_days(year_path):
	days = {}
	for child in year_path.iterdir():
		if not child.is_file():
			continue
		match = re.fullmatch(r'day([0-9]+).py', child.name, flags=re.IGNORECASE)
		if match is None:
			continue
		days[int(match.group(1))] = child
	return days

def prompt(year, year_default, day_default):
	year_resp = None
	day_resp = None
	day = None
	
	while True:
		if year is None:
			day = None
			year_resp = input(f"Year (default: {year_default}): ").lower()
			if year_resp in ("q", "quit"):
				return None, None, None, year_default, day_default
			elif year_resp == "":
				year = year_default
			elif year_resp == "latest" or re.fullmatch(r"[0-9]+", year_resp):
				year = year_resp
			else:
				print(f"Invalid year '{year_resp}'. Valid options are: {', '.join(map(str, get_years().keys()))}, or latest")
			continue
		else:
			years = get_years()
			if year == "latest":
				year = max(years.keys())
			year = int(year)
			if year not in years:
				print(f"Invalid year '{year_resp}'. Valid options are: {', '.join(map(str, get_years().keys()))}, or latest")
				year = None
				continue
		
		if day is None:
			day_resp = input(f"Day (default: {day_default}): ").lower()
			if day_resp in ("q", "quit"):
				year = None
			elif day_resp == "":
				day = day_default
			elif day_resp == "latest" or re.fullmatch(r"[0-9]+", day_resp):
				day = day_resp
			else:
				print(f"Invalid day '{day_resp}'. Valid options are: {', '.join(map(str, get_days(years[year]).keys()))}")
			continue
		else:
			days = get_days(years[year])
			if day == "latest":
				day = max(days.keys())
			day = int(day)
			if day not in days:
				print(f"Invalid day '{day_resp}'. Valid options are: {', '.join(map(str, get_days(years[year]).keys()))}")
				day = None
				continue
		
		break
	
	year_default = year_resp or year_default
	day_default = day_resp or day_default

	return year, day, days[day], year_default, day_default

def import_solver(path):
	parts = __name__.rpartition(".")[0].split(".")
	parts += list(path.with_suffix("").relative_to(Path(__file__).parent).parts)
	name = ".".join(parts)

	if name in sys.modules:
		module = importlib.reload(sys.modules[name])
	else:
		module = importlib.__import__(name, fromlist="Solver")

	return module.Solver


def main():
	year = None
	year_default = "latest"
	day_default = "latest"

	try:
		print("Welcome to Tinynja's Advent Of Code solutions!")

		while True:
			year, day, day_path, year_default, day_default = prompt(year, year_default, day_default)
			if year is None:
				break
			
			print(f"~~~~~~~~~~~~~ {year} - Day {day} ~~~~~~~~~~~~~")
			try:
				Solver = import_solver(day_path)
				solver = Solver()
				solver.solve1()
				print("Part 1:", solver.part1)
				solver.solve2()
				print("Part 2:", solver.part2)
			except:
				print(format_exc())
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	except KeyboardInterrupt:
		pass


if __name__ == "__main__":
	main()