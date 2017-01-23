#!/usr/bin/env python

def frange(stop, start = 0, increment = 1):
	x = start
	while x < stop:
		yield x
		x += increment

for n in frange(10, 1.0, 0.5):
	print(n)


"""
一个函数如果存在yield语句，那么则其就是一个生成器。
生成器只能用于迭代操作。（不同于其他普通的函数）

"""

def countdown(n):
	print("Starting to count from", n)
	while  n > 0:
		yield n
		n -= 1
	print ("Done!")

c = countdown(3)
print (c)

print(next(c))
print(next(c))
print(next(c))
print(next(c)) #打印Done!并出错

"""
总结:
	一个生成器函数主要特征，它会回应在迭代器中使用next操作。
	一旦生成器函数返回退出，迭代终止。

"""