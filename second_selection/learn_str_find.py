#!/usr/bin/env python

text = 'yeah, but no, but yeah, but no, but yeah'

#完全匹配
resval = text == 'yeah'
print(resval) #->False

#start or end
resval = text.startswith("yeah")
print (resval)#->True
resval = text.endswith("no")
print (resval)#->False

# find the first occurrence
resval = text.find('no')
print (resval)#->10

# 正则表达式
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

"""
match() 总是从字符串开始去匹配，
如果想查找字符串任意部分的的模式出现的位置，使用findall() 方法

"""
import re
if re.match(r'\d+/\d+/\d+', text1):
	print("y")
else:
	print ("n")
#->y
if re.match(r'\d+/\d+/\d+', text2):
	print("y")
else:
	print ("n")
#->n

#将模式字符串编译成模式对象
datepat = re.compile(r"\d+/\d+/\d+")

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
resval = datepat.findall(text)
print (resval) #->['11/27/2012', '3/13/2013']

#使用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match("11/27/2012")
print(m)
print(m.group()) #-> 11/27/2012默认值是0
print(m.group(0)) #->11/27/2012
print(m.group(1)) #->11
print(m.group(2)) #->27
print(m.group(3)) #->2012
print(m.groups()) #->('11', '27', '2012')
month, day, year = m.groups()

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
resval = datepat.findall(text)
print (resval) #-> [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
	print ("{}-{}-{}".format(year, month, day))
"""
2012-11-27
2013-3-13
"""

"""
findall() 方法会搜索文本并以列表形式方法所有的匹配，
如果想以迭代方式匹配，可以使用finditer()方法来代替。
"""
for m in datepat.finditer(text):
	print (m) # 返回每一个match对象，可以在match对象上调用groups来处理


# 正则表达式说明
"""
编译对象: re.comile()
match对象: match(),  finditer()
结果集:findall()
"""

"""
match 仅仅检查字符串的开始部分
"""
m = datepat.match('11/27/2012abcdef')
print (m.group()) #->11/27/2012

"""
如果你想精确匹配，确保你的正则表达式以$结尾
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')

"""
忽略编译部分（使用一次）
"""
re.findall(r'(\d+)/(\d+)/(\d+)', text)
