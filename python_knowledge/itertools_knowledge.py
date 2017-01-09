#!/usr/bin/env python

from itertools import count
from itertools import cycle
from itertools import repeat

#无限循环
#从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
"""
def count(start=0, step=1):
	n = start
	while True:
		yield n
		n += start

"""
print (next(count(5,2)))

#重复序列的元素，既a, b, c, a, b, c ...
"""
def cycle(iterable):
	saved = []
	for element in iterable:
		yield element
		saved.append(element)
	while saved:
		for element in saved:
			yield element
"""
print (next(cycle('abc')))

#重复
"""
def repeat(obj, times=None):
	if itmes is None:
		while True:
			yield obj
	else:
		for i range(times):
			yield obj
"""
print (next(repeat(1.2)))

#重复10，共重复5次
print (next(repeat(10, 5)))

#函数式工具
"""
将函数本身作为处理对象的编程范式，
在Python中，函数也是对象，因此可以轻松的进行一些函数式的处理，
比如map(), filter(), reduce() 函数

itertools包含类似的工具。这些函数接收函数作为参数，并将结果返回为一个循环器。
"""

#累积
"""
def accumulate(iterable, func=operator.add):
	it = iter(iterable)
	try:
		total = next(it)
	except StopIteration:
		return 
	yield total
	for element in it:
		total = func(total, element)
		yield total
"""
from itertools import accumulate
from operator import sub
a = accumulate([1,2,3,4,5])
a = accumulate([1,2,3,4,5], sub)
print(list(a))













from itertools import starmap

#依次将 序列中的值传递给pow函数（多次调用一个函数）

"""
def starmap(function, iterable):
	for args in iterable:
		yield function(*args)
"""
a = starmap(pow, [(1, 1),(2, 2), (3, 3)])
print (list(a))


#组合工具
#连接
"""
def chain(*iterables):
	for it in iterables:
		for element in it:
			yield element
"""
from itertools import chain
c = chain([1,2,3], "abc", "def")
print (list(c))

# 从一个列表中获取
"""
def from_iterable(iterables):
	for it in iterables:
		for element in it:
			yield element
"""
d = chain.from_iterable(['abc', 'edf'])
print (list(d))

#其他

#根据一组Ture/False选择值
"""
def compress:
	return (d for d,s in zip(data, selectors) if s)
"""
from itertools import compress
c = compress('abc', [1, 0, 1])
print (list(c))


# 截取第一个不满足条件的序列到结尾
"""
def (predicate, iterable):
	iterbale = iter(iterable)

	for x in iterable:
		if not predicate(x):
			yield x
			break
	#迭代下面的元素
	for x in iterable:
		yield x
"""

from itertools import dropwhile
d = dropwhile(lambda x : x > 6, (7, 8, 3, 4, 5, 7, 8))
print(list(d))


# 过滤值返回值为false的iterbale
"""
def filterfalse(predicate, iterable):
	if predicate is None:
		predicate = bool
	for x in iterable:
		if not predicate(x):
			yield x
"""
from itertools import filterfalse
f = filterfalse(None, ["aa", "", 0, "v", 0.0])
print (list(f))
