
import re
class Regex:
	def __init__(self,text):
		self.__text = text
	def parse(self,pattern):
		ending = list(pattern)
		if ' ' in pattern:
			pattern.insert(0,'[^\s')
			ending.insert(0,'[\s')
		else:
			pattern.insert(0,'[^')
			ending.insert(0,'[')
		ending.append(']')
		ending = ''.join(str(x) for x in ending)
		pattern.append(']+|' + ending )
		pattern = ''.join(str(x) for x in pattern)
		pattern = re.compile(pattern,re.L)
		return pattern.findall(self.__text.strip())
a = Regex('this is me.and you*')
print(a.parse('/'))




