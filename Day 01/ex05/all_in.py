#!/usr/bin/python3

import sys

def find_info(i):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	try:
		print(str(capital_cities[str(states[i.title().strip()])]) + " is the capital of " + i.title().strip())
	except:
		for key, value in capital_cities.items():
			if i.title().strip() == value:
				for state, code in states.items():
					if key == code:
						print(i.title().strip() + " is the capital of " + state)
						return
				print(i.strip() + " is neither a capital city nor a state")
				return
		print(i.strip() + " is neither a capital city nor a state")

def get_info(param):
	
	arr = str(param).split(",")
	for i in arr:
		if (i.strip() != ""):
			find_info(i);
	


if __name__ == '__main__':
	if len(sys.argv) == 2:
		get_info(str(sys.argv[1]))