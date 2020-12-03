# ~~~~~~~~~ Built-in libraries ~~~~~~~~~
import os, re, importlib, sys
from functools import partial
from configparser import ConfigParser
from traceback import format_exc
# ~~~~~~~~~~~ Pipy libraries ~~~~~~~~~~~
import clipboard


# ~~~~~~~~~~ Useful functions ~~~~~~~~~~
list_years = lambda: {int(f[3:]):f for f in os.listdir() if os.path.isdir(f) and re.fullmatch(r'(?i)AOC[0-9]+', f)}
list_days = lambda year: {int(re.search(r'[0-9]+', f).group()):os.path.splitext(f)[0] for f in os.listdir(os.path.join(list_years()[year], 'days')) if re.fullmatch(r'(?i)day[0-9]+.py', f)}

def input_and_verify(text, verifier):
	while True:
		userinput = input(text)
		if verifier(userinput): break
		print('Invalid input.')
	return userinput


# ~~~~~~~~~ Config read/setup ~~~~~~~~~
config = ConfigParser()
config.read('default.cfg')

re_year = re.compile(r'(?i)exit|q|([0-9]+|last)\/([0-9]+|last)|[0-9]+' + ('|' if 'year' in config.defaults() else ''))
re_day = re.compile(r'(?i)exit|q|last|[0-9]+' + ('|' if 'day' in config.defaults() else ''))

if 'year' in config.defaults():
	ui_input = config.defaults()['year']
	keep_input = True
	if 'day' in config.defaults():
		ui_input += '/' + config.defaults()['day']
else:
	ui_input = ''
	keep_input = False


# ~~~~~~~~~~~~~ Main loop ~~~~~~~~~~~~~
year, day = '', ''

print(f'Welcome to Tinynja\'s Advent Of Code solutions!')

while True:
	if year == '':
		if not keep_input: ui_input = input_and_verify(f"""Year {(f'(default:={config.defaults()["year"]})' if 'year' in config.defaults() else '')}: """, re_year.fullmatch)
		if ui_input == '' and 'year' in config.defaults():
			ui_input = config.defaults()['year']
		if ui_input in ('exit','q'):
			break
		else:
			keep_input = False
			ui_input = ui_input.split('/')
			if ui_input[0] == 'last' and len(list_years()) > 0:
				year = max(list_years())
			elif int(ui_input[0]) in list_years():
				year = int(ui_input[0])
			else:
				print(f'Year {ui_input[0]} has not yet been solved. Get to work or be patient!')
			if len(ui_input) == 2:
				ui_input = ui_input[1]
				keep_input = True

	if year != '' and day == '':
		if not keep_input: ui_input = input_and_verify(f"""Day {(f'(default:={config.defaults()["day"]})' if 'day' in config.defaults() else '')}: """, re_day.fullmatch)
		keep_input = False
		if ui_input == '' and 'day' in config.defaults():
			ui_input = config.defaults()['day']
		if ui_input == 'exit':
			break
		elif ui_input == 'q':
			year = ''
		elif ui_input == 'last' and len(list_days(year)) > 0:
			day = max(list_days(year))
		elif re.match(r'[0-9]+', ui_input) and int(ui_input) in list_days(year):
			day = int(ui_input)
		else:
			print(f'Day {ui_input} of year {year} has not yet been solved. Get to work or be patient!')

	if year in list_years() and day in list_days(year):
		print(f'~~~~~~~~~~ {year:4} - Day {day:02} ~~~~~~~~~~')
		try:
			module = None
			if (module_name := list_years()[year] + '.days.' + list_days(year)[day]) in sys.modules:
				module = importlib.reload(sys.modules[module_name])
			elif (spec := importlib.util.find_spec(module_name)) is not None:
				module = importlib.util.module_from_spec(spec)
				sys.modules[module_name] = module
				spec.loader.exec_module(module)
			# else:
			# 	module = importlib.import_module(module_name)
			if module is None:
				raise ImportError(f'day {day} couldn\'t be imported')
			elif not hasattr(module, f'Day{day}'):
				raise NameError(f'day {day} has been imported but class "Day{day}" is missing')
			else:
					solver = getattr(module, f'Day{day}')()
					for i in range(1,3):
						print(f'Part {i}: ', end='')
						try:
							getattr(solver, f'solve{i}')()
							try:
								print(getattr(solver, f'part{i}'))
								clipboard.copy(getattr(solver, f'part{i}'))
							except AttributeError:
								print('Solution missing.')
						except NotImplementedError:
							print('Not implemented yet.')
		except:
			print(format_exc())
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		day = ''