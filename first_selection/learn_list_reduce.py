#!/usr/bin/env python
# coding=utf-8

#缺陷，如果数据量大的话，将会产生非常大的结果集
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

newList = [i for i in mylist if i > 0]
print(type(newList)) # -><class 'list'>
print(newList) #->[1, 4, 10, 2, 3]

#列表推导可以操作
newList = [i + 1 for i in mylist if i > 0]
print(newList) #->[2, 5, 11, 3, 4]

#过滤变种，将不符合的值变掉，而不是删除它们
newList = [n if n > 0 else 0 for n in mylist]
print(newList) #->[1, 4, 0, 10, 0, 2, 3, 0]




#生成器表达式
newList = (i for i in mylist if i > 0)
print (type(newList)) # -> <class 'generator'>

#内建函数filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

#filter 返回一个迭代器
isVals = list(filter(is_int, values))
print(isVals) #->['1', '2', '-3', '4', '5']


# itertools.compress()
addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK'
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5) #[False, False, True, False, False, True, True, False]

newList = list(compress(addresses, more5))
print(newList) #['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']




