#!/usr/bin/env python

import re
text = 'UPPER PYTHON, lower python, Mixed Python'

resval = re.findall('python', text, flags=re.IGNORECASE)
print(resval) #['PYTHON', 'python', 'Python']

resval = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(resval) #UPPER snake, lower snake, Mixed snake

def matchcase(word):
	def replace(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		elif text.islower():
			return word.lower()
		elif text[0].isupper():
			return word.capitalize()
		else:
			return word
	return replace

resval = re.sub("python", matchcase('snake'), text, flags=re.IGNORECASE)
print(resval) #->UPPER SNAKE, lower snake, Mixed Snake


