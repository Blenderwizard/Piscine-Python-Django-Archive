#!/usr/bin/python3

class Intern:
	def __init__(self, name="My name? I'm nobody, an intern, I have no name.") -> None:
		self.name = name
	
	def __str__(self) -> str:
		return self.name

	class Coffee:
		def __str__(self) -> str:
			return "This is the worst coffee you ever tasted."

	def work(self) -> str:
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self) -> Coffee:
		return self.Coffee()

def tests():
	intern1 = Intern()
	intern2 = Intern("Mark")

	print(intern1)
	print(intern2)

	print()
	print(str(intern2) + " makes coffee. " + str(intern2.make_coffee()))
	print()
	try:
		intern1.work()
	except Exception as err:
		print(err)

if __name__ == '__main__':
	tests()