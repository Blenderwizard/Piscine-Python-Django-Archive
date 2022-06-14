#!/usr/bin/python3

import random

from beverages import *

class CoffeeMachine:
	def __init__(self) -> None:
		self.uses = 10

	class EmptyCup(HotBeverage):
		def __init__(self) -> None:
			self.price = 0.9
			self.name = "empty cup"

		def description(self) -> str:
			return "An empty cup?! Gimme my money back"
	
	class BrokenMachineException(Exception):
		def __init__(self) -> None:
			super().__init__("This coffee machine has to be repaired.")
	
	def repair(self) -> None:
		self.uses = 10

	def serve(self, request: HotBeverage) -> HotBeverage:
		if (self.uses == 0):
			raise self.BrokenMachineException()
		self.uses -= 1
		return random.choice([HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino(), self.EmptyCup()])

def tests() -> None:
	machine = CoffeeMachine()

	for i in range(22):
		try:
			result = machine.serve(Tea())
			print("Print I want Tea")
			print("I got:")
			print(result)
		except Exception as err:
			print(err)
			machine.repair()
		print()
	

if __name__ == '__main__':
	tests()