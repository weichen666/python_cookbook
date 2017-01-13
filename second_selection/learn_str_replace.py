#!/usr/bin/env python

text = 'yeah, but no, but yeah, but no, but yeah'
#全部替换
text = text.replace('yeah', 'yep')
print(text) #->yep, but no, but yep, but no, but yep

#正则表达式
"""
sub() 函数
	1. 传递正则
		第一次参数为匹配的模式
		第二个参数为替换模式(可以使用\数字指向前面模式的捕获组号)
	2. 传递回调函数
		回调函数的参数是一个match对象，回调函数返回最终被替换的字符串
subn() 函数
	查看有多少替换发生了

"""
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re

resval = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print (resval) #Today is 2012-11-27. PyCon starts 2013-3-13.

#传递回调函数
from calendar import month_abbr
def chane_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return "{}-{}-{}".format(m.group(2), mon_name, m.group(3))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

resval = datepat.sub(chane_date, text)
print(resval) #->Today is 27-Nov-2012. PyCon starts 13-Mar-2013.