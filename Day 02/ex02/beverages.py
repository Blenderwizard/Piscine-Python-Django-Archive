#!/usr/bin/python3

class HotBeverage:
	def __init__(self) -> None:
		self.price = 0.3
		self.name = "hot beverage"
	
	def description(self) -> str:
		return "Just some hot water in a cup."
	
	def __str__(self) -> str:
		return "name: " + self.name + "\nPrice: {price:.2f}".format(price=self.price) + "\ndescription: " + self.description()

class Coffee(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.4
		self.name = "coffee"

	def description(self) -> str:
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.3
		self.name = "tea"
	
class Chocolate(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.5
		self.name = "chocolate"

	def description(self) -> str:
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self) -> None:
		self.price = 0.45
		self.name = "cappuccino"

	def description(self) -> str:
		return "Un po' di Italia nella sua tazza!"

def tests():
	hotb = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	choco = Chocolate()
	cap = Cappuccino()

	print(hotb, end='\n\n')
	print(coffee, end='\n\n')
	print(tea, end='\n\n')
	print(choco, end='\n\n')
	print(cap)



if __name__ == '__main__':
	tests()