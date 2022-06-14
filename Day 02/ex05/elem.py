#!/usr/bin/python3

class Text(str):
	"""
	A Text class to represent a text you could use with your HTML elements.

	Because directly using str class was too mainstream.
	"""

	def __str__(self):
		"""
		Do you really need a comment to understand this method?..
		"""
		return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('\n', '\n<br />\n').replace('"', '&quot;')


class Elem:
	"""
	Elem will permit us to represent our HTML elements.
	"""

	class ValidationError(Exception):
		def __init__(self):
			super().__init__(self, "Validation Error")

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		"""
		__init__() method.

		Obviously.
		"""
		self.tag = tag
		self.attr = attr
		if type(content) == str:
			raise self.ValidationError()
		self.content = content
		self.tag_type = tag_type

	def __str__(self):
		"""
		The __str__() method will permit us to make a plain HTML representation
		of our elements.
		Make sure it renders everything (tag, attributes, embedded
		elements...).
		"""
		result = ''
		if self.tag_type == 'double':
			if self.content != None:
				result = '<' + self.tag + self.__make_attr() + '>' + self.__make_content() + '</' + self.tag + '>'
			else:
				result = '<' + self.tag + self.__make_attr() + '></' + self.tag + '>'
		elif self.tag_type == 'simple':
			result = '<' + self.tag + self.__make_attr() + ' />'
		return result

	def __make_attr(self):
		"""
		Here is a function to render our elements attributes.
		"""
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		"""
		Here is a method to render the content, including embedded elements.
		"""
		result = ''
		if type(self.content) != list and type(self.content) != Text and self.check_type(self.content):
			result = '\n' + str(self.content) + '\n'
			return "  ".join(line for line in result.splitlines(True))
		elif type(self.content) == Text and self.content != '':
			result = '\n' + str(self.content) + '\n'
			return "  ".join(line for line in result.splitlines(True))
		elif len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			if str(elem) != '':
				result += str(elem) + '\n'
		if result == '\n':
			result = ''
		return "  ".join(line for line in result.splitlines(True))
		

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		"""
		Is this object a HTML-compatible Text instance or a Elem, or even a
		list of both?
		"""
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))


# <html>
#   <head>
#     <title>
#       "Hello ground!"
#     </title>
#   </head>
#   <body>
#     <h1>
#       "Oh no, not again!"
#     </h1>
#     <img src="http://i.imgur.com/pfp3T.jpg" />
#   </body>
# </html>

def test() -> None:
	print(Elem(tag = 'html', content = [ \
		Elem(tag = 'head', content = \
			Elem(tag='title', content=Text('"Hello ground!"'))), \
		Elem(tag='body', content= [ \
			Elem(tag='h1', content=Text('"Oh no, not again!"')), \
			Elem(tag='img', attr= {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple') \
		]) \
	]))


if __name__ == '__main__':
	test()
