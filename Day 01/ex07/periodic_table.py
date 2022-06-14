#!/usr/bin/python3

import sys

def generate_blank(tabs: int, out):
	out.write(("\t" * tabs) + "<td class=\"blank\"></td>\n")

def generate_element(arr: list, tabs: int, out):
	pos = {
		'ng': [2, 10, 18, 36, 54, 86],
		'rnm': [1,6,7,8,9,15,16,17,34,35,53],
		'ml': [5,14,32,33,51,52,85],
		'ptm': [13,31,49,50,81,82,83,84],
		'aem': [4,12,20,38,56,88],
		'am': [3,11,19,37,55,87],
		'unk': [109,110,111,112,113,114,115,116,117,118],
	}
	number = int(str(arr[1]).rpartition(":")[2].strip())
	astr = "tm"
	for fam, mem in pos.items():
		for ind in mem:
			if (ind == number):
				astr = fam

	out.write(("\t" * tabs) + "<td class=\"element " + astr +"\">\n")
	out.write(("\t" * (tabs + 1)) + "<h4>" + str(arr[0]).rpartition("=")[0].strip() + "</h4>\n")
	out.write(("\t" * (tabs + 1)) + "<ul>\n")
	out.write(("\t" * (tabs + 2)) + "<li class=\"number\">" + str(arr[1]).rpartition(":")[2].strip() + "</li>\n")
	out.write(("\t" * (tabs + 2)) + "<li class=\"shortname\"><b>" + str(arr[2]).rpartition(":")[2].strip() + "</b></li>\n")
	out.write(("\t" * (tabs + 2)) + "<li class=\"molar\">" + str(arr[3]).rpartition(":")[2].strip() + "</li>\n")
	out.write(("\t" * (tabs + 2)) + "<li class=\"electron\">" + str(arr[4]).rpartition(":")[2].strip() + "</li>\n")
	out.write(("\t" * (tabs + 1)) + "</ul>\n")
	out.write(("\t" * tabs) + "</td>\n")

def generate_periodic_rows(Lines: list, tabs: int, out):
	out.write(("\t" * tabs) + "<tr>\n")
	last = 0
	for line in Lines:
		arr = line.strip().split(',');
		if last == int(str(arr[0]).rpartition(":")[2].strip()):
			generate_element(arr, tabs + 1, out)
			last += 1
		else:
			while last != int(str(arr[0]).rpartition(":")[2].strip()):
				generate_blank(tabs + 1, out)
				last += 1
			generate_element(arr, tabs + 1, out)
			last += 1
		if last == 18:
			last = 0
			out.write(("\t" * tabs) + "</tr>\n")
			if Lines.index(line) != len(Lines) - 1:
				out.write(("\t" * tabs) + "<tr>\n")

def generate_periodic_table(tabs: int, out):
	f = open('periodic_table.txt', 'r')
	Lines = f.readlines()
	out.write(("\t" * tabs) + "<table>\n")
	generate_periodic_rows(Lines, tabs + 1, out)
	out.write(("\t" * tabs) + "</table>\n")
	f.close()

def generate_file():
	out = open("periodic_table.html", "w")
	out.write("<!DOCTYPE html>\n")
	out.write("<html lang=\"en\">\n")
	out.write(("\t" * 1) + "<head>\n")
	out.write(("\t" * 2) + "<style>\n")
	out.write(("\t" * 3) + "body {\n")
	out.write(("\t" * 4) + "margin: 0;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "table, tr, th, td {\n")
	out.write(("\t" * 4) + "border-collapse: collapse;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "td {\n")
	out.write(("\t" * 4) + "border: solid;\n")
	out.write(("\t" * 4) + "width: 5%;\n")
	out.write(("\t" * 4) + "height: 7%;\n")
	out.write(("\t" * 4) + "background-clip: padding-box;\n")
	out.write(("\t" * 4) + "position: relative;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "tr {\n")
	out.write(("\t" * 4) + "width: 100%;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "table {\n")
	out.write(("\t" * 4) + "table-layout: fixed;\n")
	out.write(("\t" * 4) + "width: 100%;\n")
	out.write(("\t" * 4) + "height: 100vh;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "ul {\n")
	out.write(("\t" * 4) + "list-style-type: none;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + "h4 {\n")
	out.write(("\t" * 4) + "position: absolute;\n")
	out.write(("\t" * 4) + "top: 50%;\n")
	out.write(("\t" * 4) + "left: 50%;\n")
	out.write(("\t" * 4) + "transform: translate(-50%, -50%);\n")
	out.write(("\t" * 4) + "margin: 0 auto;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".blank {\n")
	out.write(("\t" * 4) + "border: transparent;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".number {\n")
	out.write(("\t" * 4) + "position: absolute;\n")
	out.write(("\t" * 4) + "margin: 0 auto;\n")
	out.write(("\t" * 4) + "top: 0px;\n")
	out.write(("\t" * 4) + "right: 0px;\n")
	out.write(("\t" * 4) + "font-size: smaller;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".shortname {\n")
	out.write(("\t" * 4) + "position: absolute;\n")
	out.write(("\t" * 4) + "margin: 0 auto;\n")
	out.write(("\t" * 4) + "top: 0px;\n")
	out.write(("\t" * 4) + "left: 0px;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".electron {\n")
	out.write(("\t" * 4) + "position: absolute;\n")
	out.write(("\t" * 4) + "bottom: 0px;\n")
	out.write(("\t" * 4) + "left: 0;\n")
	out.write(("\t" * 4) + "margin: 0 auto;\n")
	out.write(("\t" * 4) + "font-size: smaller;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".molar {\n")
	out.write(("\t" * 4) + "position: absolute;\n")
	out.write(("\t" * 4) + "bottom: 15%;\n")
	out.write(("\t" * 4) + "left: 0;\n")
	out.write(("\t" * 4) + "margin: 0 auto;\n")
	out.write(("\t" * 4) + "font-size: smaller;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".ng {\n")
	out.write(("\t" * 4) + "background-color: purple;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: white;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".rnm {\n")
	out.write(("\t" * 4) + "background-color: limegreen;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: black;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".am {\n")
	out.write(("\t" * 4) + "background-color: indianred;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: black;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".aem {\n")
	out.write(("\t" * 4) + "background-color: goldenrod;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: black;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".tm {\n")
	out.write(("\t" * 4) + "background-color: crimson;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: black;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".ml {\n")
	out.write(("\t" * 4) + "background-color: teal;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: black;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".ptm {\n")
	out.write(("\t" * 4) + "background-color: blue;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: white;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 3) + ".unk {\n")
	out.write(("\t" * 4) + "background-color: black;\n")
	out.write(("\t" * 4) + "border-color: black;\n")
	out.write(("\t" * 4) + "color: white;\n")
	out.write(("\t" * 3) + "}\n")
	out.write(("\t" * 2) + "</style>\n")
	out.write(("\t" * 2) + "<title>Periodic Table of Elements</title>\n")
	out.write(("\t" * 1) + "</head>\n")
	out.write(("\t" * 1) + "<body>\n")
	generate_periodic_table(2, out);
	out.write(("\t" * 1) + "</body>\n")
	out.write("</html>\n")
	out.close()



if __name__ == '__main__':
	generate_file()