from elements import *

class Page:
	def __init__(self, page: Elem) -> None:
		self.page = page

	def is_valid(self) -> bool:
		if type(self.page) == list:
			for element in self.page:
				if self.__is_valid_helper(element.content, element) == False:
					return False
			return True
		bol = self.__is_valid_helper(self.page.content, self.page)
		return bol

	def __str__(self) -> str:
		ret = ''
		if type(self.page) == Html:
			ret = '<!DOCTYPE html>\n'
		if type(self.page) == list:
			if len(self.page) == 1 and type(self.page[0]) == Html:
				ret = '<!DOCTYPE html>\n'
			for element in self.page:
				ret += str(element)
				if self.page.index(element) != len(self.page)-1:
					ret += '\n'
			return ret
		return ret + str(self.page)

	def write_to_file(self,path: str) -> None:
		try:
			f = open(path, 'w')
			f.write(str(self.page))
			f.close()
		except:
			print("An error occured while atempting write to the file")

	def __is_valid_helper(self, page: Elem, lastpage=None) -> bool:
		valid_types = [Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td , Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text, list, None]
		if type(page) not in valid_types:
			return False
		elif type(lastpage) == Html:
			if type(page) != list and len(page) != 2:
				return False
			if type(page[0]) != Head or type(page[1]) != Body:
				return False
			if type(page[0].content) == list:
				for element in page[0].content:
					if self.__is_valid_helper(element.content, element) == False:
						return False
			else: 
				if self.__is_valid_helper(page[0].content.content, page[0].content) == False:
					return False
			if type(page[1].content) == list:
				for element in page[1].content:
					if self.__is_valid_helper(element.content, element) == False:
						return False
			else:
				if self.__is_valid_helper(page[1].content.content, page[1].content)== False:
					return False
		elif type(lastpage) == Head:
			if type(page) != Title and not(type(page) == list and len(page) == 1):
				return False
			if type(page) == list and type(page[0]) != Title:
				return False
			if type(page) == list:
				return self.__is_valid_helper(page.content[0], page)
			else:
				return self.__is_valid_helper(page.content, page)
		elif type(lastpage) == Body or type(lastpage) == Div:
			valid_types = [H1, H2, Div, Table, Ul, Ol, Span, Text, list, None]
			if type(page) not in valid_types:
				return False
			if type(page) == list:
				for element in page:
					if type(element) not in valid_types:
						return False
					elif self.__is_valid_helper(element.content, element) == False:
						return False
			else:
				return self.__is_valid_helper(page.content, page)
		elif type(lastpage) in [Title, H1, H2, Li, Th, Td]:
			if type(page) != Text and not(type(page) == list and len(page) == 1):
				return False
			if type(page) == list and type(page[0]) != Text:
				return False
		elif type(lastpage) == P:
			if type(page) != Text and type(page) != list:
				return False
			if type(page) == list:
				for element in page:
					if type(element) != Text:
						return False
		elif type(lastpage) == Span:
			if type(page) != Text and type(page) == list:
				return False
			if type(page) == list:
				if len(page) == 0:
					if type(page[0]) != Text and type(page[0]) != P:
						return False
				else:
					for element in page:
						if type(element) != P:
							return False
						ret = self.__is_valid_helper(element.content, element)
						if ret == False:
							return False
		elif type(lastpage) == Ul and type(lastpage) == Ol:
			if type(page) != Li and type(page) != list:
				return False
			if type(page) == list:
				for element in page:
					if type(element) != Li:
						return False
					ret = self.__is_valid_helper(element.content, element)
					if ret == False:
						return False
			return self.__is_valid_helper(page)
		elif type(lastpage) == Tr:
			if type(page) != Td and type(page) != Th and type(page) != list:
				return False
			if type(page) == list:
				hasTd = False
				hasTh = False
				for element in page:
					if type(element) != Td and type(element) != Th:
						return False
					if type(element) == Td:
						hasTd = True
					if type(element) == Th:
						hasTh = True
					if hasTd and hasTh:
						return False
					ret = self.__is_valid_helper(element.content, element)
					if ret == False:
						return False
		elif type(lastpage) == Table:
			if type(page) != Tr and type(page) != list:
				return False
			if type(page) == list:
				for element in page:
					if type(element) != Tr:
						return False
					ret = self.__is_valid_helper(element.content, element)
					if ret == False:
						return False
		return True

def tests():
	print("Test 1:")
	t = Page(P([Text("Hello"), Text("World")]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 2:")
	t = Page(Html([Head(Title(Text("Title"))), Body(H1(Text("body")))]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 3:")
	t = Page(Html([Body(H1(Text("body")))]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 4:")
	t = Page(Html([Head(Title(Text("Title"))), Body(Table([Tr([Th(Text("Title")), Th(Text("Title")), Th(Text("Title"))]),Tr([Td(Text("Title")), Td(Text("Title")), Td(Text("Title"))])]))]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 5:")
	t = Page(Html([Head(Title(Text("Title"))), Body(Table([Tr([Th(Text("Title")), Th(Text("Title")), Th(Text("Title"))]),Tr([Th(Text("Title")), Td(Text("Title")), Td(Text("Title"))])]))]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 6:")
	t = Page([Ul([Li(Text("1")), Li(Text("2")), Li(Text("3"))]), Ol([Li(Text("1")), Li(Text("2")), Li(Text("3"))])])
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 7:")
	t = Page([Html()])
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print()

	print("Test 8:")
	t = Page(Html([Head(Title(Text('"Hello ground!"'))), Body([H1(Text('"Oh no, not again!"')), Img(attr= {'src': 'http://i.imgur.com/pfp3T.jpg'})])]))
	print(t)
	print("Is valid: " + str(t.is_valid()))
	print("writing Output")
	t.write_to_file("file.html")

if __name__ == '__main__':
	tests()