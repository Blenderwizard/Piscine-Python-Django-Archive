from django.shortcuts import render

class Color:
	def __str__(self):
		temp = self.color
		if (self.name == "Black"):
			self.color = str(hex(int("0x" + self.color.removeprefix("#"), 16) + int("0x050505", 16))).removeprefix("0x")
			if (len(self.color) == 5):
				self.color = "0" + self.color
		elif (self.name == "Blue"):
			self.color = str(hex(int("0x" + self.color.removeprefix("#"), 16) + int("0x050500", 16))).removeprefix("0x")
			if (len(self.color) == 5):
				self.color = "0" + self.color
		elif (self.name == "Green"):
			self.color = str(hex(int("0x" + self.color.removeprefix("#"), 16) + int("0x050005", 16))).removeprefix("0x")
			if (len(self.color) == 5):
				self.color = "0" + self.color
		elif (self.name == "Red"):
			self.color = str(hex(int("0x" + self.color.removeprefix("#"), 16) + int("0x000505", 16))).removeprefix("0x")
			if (len(self.color) == 5):
				self.color = "0" + self.color
		self.color = "#" + self.color
		return (temp)

	def __init__(self, color:str, name:str) -> None:
		self.color = color
		self.name = name

def index(request):
	return render(request, 'ex03/index.html', {
		"rows" : range(0,50),
		"cols": [Color("#000000", "Black"), Color("#FF0000", "Red"), Color("#0000FF", "Blue"), Color("#00FF00", "Green")]
	})