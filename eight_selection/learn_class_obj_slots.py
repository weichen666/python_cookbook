#!/usr/bin/env python

class Date:
	"""
		当定义了__slots__属性时，
		ython就会针对实例采用一种更加紧凑的内部表示，
		不在让每个实例都创建一个__dict__字典。
		实例通过一个很小的固定大小的数组来创建，
		在__slots__中列出的属性名会在内部映射到这个数组的指定下标上。
		但是，我们创建的实例属性就无法在添加新的属性了。
		只能使用在__slots__中定义的那些属性名。
	"""
	__slots__ = ['year', 'month', 'day']
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

