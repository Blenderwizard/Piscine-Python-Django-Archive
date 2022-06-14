#!/usr/bin/python3

def numbers():
	with open("numbers.txt", 'r') as f:
		str = ''
		char = f.read(1)
		while char:
			str += char
			char = f.read(1)
		for i in str.split(','):
			try:
				print(int(i.strip()))
			except:
				continue
		f.close()
		

if __name__ == '__main__':
	numbers()