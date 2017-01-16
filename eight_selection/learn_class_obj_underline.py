#!/usr/bin/env python

class A:
	def __init__(self):
		self._internal = 0
		self.public = 1

	def public_method(self):
		"""
			a public method
		"""

	def _internal_method(slef):
		;

"""
Python并不会真的阻止别人访问内部名称。但是如果你这么做肯定是不好的，
可能会导致脆弱的代码。

已下划线大头的标识也可以用于模块名称和模块级别的函数中。
如果见到一模块已_开始（_socket），则它属性内部实现。
比如 sys._getframe() 使用起来要特别注意
"""

class B:
	def __init__(self):
		self._private = 0

	def __private_method(self):
		;

	def public_method(self):
		self.__private_method()

"""
双下滑线打头的名称会导致出现名称重整(name mangling)的行为。
也就是，这个类中的私有属性会被分别重命名为_B__private和_B__private_method
目的：
	为了继承，这样的属性不能通过继承覆盖。

"""

class C(B):
	def __init__(self):
		super().__init__()
		self._private = 1 # 并不是重写了B._private

"""
	私有名字_private 会被重命名为_C__private 和B中的重整名称不同。
"""

"""
应该使用那个?

	(1) 让非公有名称以单下划线开头。
	(2) 如果涉及到子类化处理，而且有些内部属性应该对子类进行隐藏，那么就使用双下划线开始
	(3) 为了解决和关键字冲突，可以使用 在关键字后面加一个下划线如	case_.
 
"""


















