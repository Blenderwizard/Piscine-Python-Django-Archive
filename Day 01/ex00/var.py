#!/usr/bin/python3

def my_var():
	var = 42
	print(str(var) + " has a type " + str(type(var)))
	var = "42"
	print(str(var) + " has a type " + str(type(var)))
	var = "quarante-deux"
	print(str(var) + " has a type " + str(type(var)))
	var = 42.0
	print(str(var) + " has a type " + str(type(var)))
	var = True
	print(str(var) + " has a type " + str(type(var)))
	var = [42]
	print(str(var) + " has a type " + str(type(var)))
	var = {42: 42}
	print(str(var) + " has a type " + str(type(var)))
	var = (42,)
	print(str(var) + " has a type " + str(type(var)))
	var = set()
	print(str(var) + " has a type " + str(type(var)))

if __name__ == '__main__':
	my_var()