#!/usr/bin/env python
#coding= utf-8

def manual_iter():
	with open("info.txt", 'rb') as f:
		try:
			while True:
				line = next(f)
				print (line.decode('utf-8'), end="")
		except StopIteration:
			pass

manual_iter()

"""
next() 还可以指定一个默认结尾值，从而不会导致异常
"""
print()
a = [1, 2]
i = iter(a)
print (next(i, None))
print (next(i, None))
print (next(i, None))
print (next(i, "xxx"))


