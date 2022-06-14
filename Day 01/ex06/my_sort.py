#!/usr/bin/python3

def my_sort():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939'
	}

	while len(d) > 0:
		l = list(d.items())
		key, low = l[0]
		low = int(low)
		for k,i in l:
			if low > int(i):
				low = int(i)
				key = k
			elif low == int(i) and key > k:
				low = int(i)
				key = k
		for k, i in d.items():
			if low == int(i) and key == k:
				print(key)
				d.pop(key)
				break
			
if __name__	== '__main__':
	my_sort()