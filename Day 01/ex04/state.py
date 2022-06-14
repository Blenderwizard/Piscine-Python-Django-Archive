#!/usr/bin/python3

import sys

def print_state(city):
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
	
	for key, value in capital_cities.items():
		if city == value:
			for state, code in states.items():
				if key == code:
					print(state)
					return
			print("Unkown capital city")
			return
	print("Unkown capital city")


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print_state(str(sys.argv[1]))