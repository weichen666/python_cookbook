#!/usr/bin/env python

#无限循环
#从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
"""
def count(start=0, step=1):
	n = start
	while True:
		yield n
		n += start

"""
from itertools import count
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
from itertools import cycle
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
from itertools import repeat
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
print(list(a)) #->[1, -1, -4, -8, -13]


#依次将 序列中的值传递给pow函数（多次调用一个函数）
from itertools import starmap
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
print (list(c)) #[1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f']

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
def dropwhile(predicate, iterable):
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

# 获取知道调用predicate(x)为False之前的数据(和dropwhile类似)
#如果第一条就不满足的话，就返回空迭代器
"""
def takewhile(predicate, iterable):
	for x in iterable:
		if predicate(x):
			yield x
		else:
			break
"""
from itertools import takewhile
t = takewhile(lambda x : x > 5, [1, 2, 3, 4, 5])
print (list(t))

#组合 group
"""
将key函数作用于原循环器的各个元素。根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。每个新的循环器以函数返回结果为标签。
这就好像一群人的身高作为循环器。
我们可以使 用这样一个key函数: 如果身高大于180，返回"tall"；如果身高底于160，返回"short";中间的返回"middle"。最终，所有身高将分为三个循环器， 即"tall", "short", "middle"。
"""

from itertools import groupby

def high_class(h):
	if h> 180:
		return "tall"
	elif h < 160:
		return "short"
	else:
		return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key=high_class)

for m,n in groupby(friends,key=high_class):
	print (m, list(n))
#注意，groupby的功能类似于UNIX中的uniq命令。
#分组之前需要使用sorted()对原循环器的元素，根据key函数进行排序，让同组元素先在位置上靠拢。

# islice() 命名切片迭代器
"""
def islice(iterable, *args):
	s = slice(*args) #生成切片对象
	it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
	
	try:
		nexti = next(it)
	except StopIteration:
		return
	for i, element in enumerate(iterable):
		if i == nexti:
			yield element
			nexti = next(it)
"""
from itertools import islice
islice("ABCDEFG", 2) #  start = 0, stop = 2, step = 1
islice("ABCDEFG", 2, 4) # start = 2, stop = 4, step = 1
islice("ABCDEFG", 2, None) # start = 2, stop = sys.maxsize, step = 1
islice("ABCDEFG", 0, None, 2) # start=2, stop=sys.maxsize, step = 2

"""
def tee(iterable, n = 2):
	it = iter(iterable)
	deques = [collections.deque() for i in range(n)]
	def gen(mydeque):
		while True:
			if not mydeque:  # when the local deque is empty
				try:
					newval = next(it)
				except StopIteration:
					return 
				for d in deques:
					d.append(newval)
			yield mydeque.popleft()
	return tuple(gen(d) for d in deques)
"""

"""从iterable创建n个独立的迭代器，创建的迭代器以n元组的形式返回，n的默认值为2，
此函数适用于任何可迭代的对象，但是，为了克隆原始迭代器，生成的项会被缓存，
并在所有新创建的迭代器中使用，
一定要注意，不要在调用tee()之后使用原始迭代器iterable，否则缓存机制可能无法正确工作
"""
from itertools import tee
t = tee([1, 2, 3])
print (list(t))


"""
操作zip 函数时，多余的话，会被截取掉
zip_longest() 则会补充fillvalue, 默认值为None
"""
from itertools import zip_longest
z = zip_longest('abc', 'bacd', fillvalue='-')
print(list(z)) #->[('a', 'b'), ('b', 'a'), ('c', 'c'), ('-', 'd')]
z = zip("abcdd", "edf")
print (list(z))
