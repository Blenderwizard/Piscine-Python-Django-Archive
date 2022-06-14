#!/usr/bin/python3

import sys

def print_capital_city(state):
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
		print(str(capital_cities[str(states[state])]))
	except:
		print("Unkown state")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		print_capital_city(str(sys.argv[1]))