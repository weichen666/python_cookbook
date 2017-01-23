#!/usr/bin/env python

class Node:
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return "Node({!r})".format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

if __name__ == "__main__":
	root = Node(0)
	c1 = Node(1)
	c2 = Node(2)
	root.add_child(c1)
	root.add_child(c2)

	for ch in root:
		print (ch)

"""
总结:
	Python 的迭代器协议需要__iter__() 方法返回一个实现了__next__() 方法的迭代器对象。

	iter() 函数的使用简化了代码，iter(s) 只是简单的通过调用s.__iter__() 方法来返回对应的迭代器对象
	

"""