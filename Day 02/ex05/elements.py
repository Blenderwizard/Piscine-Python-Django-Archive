from elem import *

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('html', attr, content, 'double')

class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('head', attr, content, 'double')

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('body', attr, content, 'double')

class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('title', attr, content, 'double')

class Meta(Elem):
	def __init__(self, attr={}):
		super().__init__('meta', attr, None, 'simple')

class Img(Elem):
	def __init__(self, attr={}):
		super().__init__('img', attr, None, 'simple')

class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('table', attr, content, 'double')

class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('th', attr, content, 'double')

class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('tr', attr, content, 'double')

class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('td', attr, content, 'double')

class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('ul', attr, content, 'double')

class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('ol', attr, content, 'double')

class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('li', attr, content, 'double')

class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('h1', attr, content, 'double')

class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('h2', attr, content, 'double')

class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('p', attr, content, 'double')

class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('div', attr, content, 'double')

class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('span', attr, content, 'double')

class Hr(Elem):
	def __init__(self, attr={}):
		super().__init__('hr', attr, None, 'simple')

class Br(Elem):
	def __init__(self, attr={}):
		super().__init__('br', attr, None, 'simple')

def test() -> None:
	print("Test 1:")
	print(Html([Head(), Body()]))
	print()

	print("Test 2:")
	print(Html( [ Head( Title( Text('"Hello ground!"'))), Body( [ H1(Text('"Oh no, not again!"')), Img(attr= {'src': 'http://i.imgur.com/pfp3T.jpg'})] )] ) )
	print()

	print("Test 3:")
	print(Html([Body([Table([Tr([Th(), Th(), Th()]), Tr([Td(), Td(), Td()]), Tr([Td(), Td(), Td()])])])]))
	print()

	print("Test 4:")
	print(Html([Head(Meta({'charset' : 'utf-8'})), Body([Br(), Hr()])]))

	print("Test 5:")
	print(Html([Body([Ol([Li(Text("Item 1")), Li(Text("Item 2")), Li(Text("Item 3"))]), Br(), Ul([Li(Text("Item 1")), Li(Text("Item 2")), Li(Text("Item 3"))])])]))
	print()

	print("Test 6:")
	print(Html([Body([Div(attr={'class':'my'}), Span(attr={'class':'my'}), H1(attr={'class':'my'}), H2(attr={'class':'my'}), P(attr={'class':'my'})])]))
	print()



if __name__ == '__main__':
	test()
