#!/usr/bin/python3

import sys
import re
import os
import settings

def fill_template(file: str):
	regex = re.compile(".*\.template")
	if not regex.match(file):
		print("Error: File does not end in template")
		return
	if not os.path.isfile(file):
		print("Error: File does not exist")
		return
	with open(file, 'r') as f:
		with open('file.html', 'w') as out:
			finalstr = ""
			char = f.read(1)
			while char:
				finalstr += char
				char = f.read(1)	
			f.close()
			out.write(finalstr.format(name=settings.name,profession=settings.profession,age=settings.age,surname=settings.surname,title=settings.title))
			out.close()	

if __name__ == '__main__':
	if len(sys.argv) == 2:
		fill_template(sys.argv[1])
	else:
		print("Error: Wrong amount of arguments")
