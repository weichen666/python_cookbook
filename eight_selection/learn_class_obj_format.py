#!/usr/bin/env python

_formats = {
	'ymd' : '{d.year}-{d.month}-{d.day}',
	'mdy' : '{d.month}/{d.day}/{d.year}',
	'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
	def __init__(self, year, month,day):
		self.year = year
		self.month = month
		self.day = day

	"""
	__format__方法给Python的字符串格式化提供了一个钩子
	格式化代码的解析工作完全由类本身决定
	"""	
	def __format__(self, code):
		if code == '':
			code = 'ymd'
		fmt = _formats[code]
		return fmt.format(d=self)

d = Date(2017, 1, 14)

print(format(d)) #->2017-1-14
print ("The date is {:ymd}".format(d))#->The date is 2017-1-14
print(format(d,'mdy')) #->1/14/2017

from datetime import date

d = date(2017, 1, 14)
print(format(d)) #->2017-01-14
print(format(d, "%A, %B %d, %Y")) #->Saturday, January 14, 2017













