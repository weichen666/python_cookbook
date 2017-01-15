#!/usr/bin/env python

class A:

	def __init__(self):
		self.x = 0

	def spam(self):
		print ("A.spam")

class B(A):

	def __init__(self):
		super().__init__() #调用父类的构造器(不需要手动的传入self)
		self.y = 1

	def spam(self):
		print ("B.spam")
		super().spam()  # call parent spam()


b = B()
b.spam()
print (b.x)


"""
覆盖特殊的方法
"""
class Proxy:
	def __init__(self, obj):
		self._obj = obj

	def __getter__(self, name):
		return getattr(self._obj, name)

	def __setattr__(self, name, value):
		if name.startswith("_"):
			super().__setattr__(name, value) # call original __setattr__
		else:
			setattr(self._obj, name, value)

p = Proxy({"a": 1, "b": 2})
print (getattr(p, "_obj")["a"])
setattr(p, "_obj", [1, 2])
print (dir(p)) 


"""
针对每一个定义的类，Python 都会计算出一个称为方法解析顺序（MRO）d的列表。
MRO只是简单地对所有基类进行线性排序。
"""

"""
要实现继承，Python从MRO列表中最左边的类开始，从左到有依次查询，直到找到带查询的属性为止


当使用super() 函数时，Python会继续从MRO中的下一个类开始搜索，
只要每一个重新定义过的方法（覆盖）都使用super(),并且只调用了它一次，
那么控制流最终就可以遍历整个MRO列表，并且让每个方法都只被执行一次。

super(), 它并不是一定要关联到某一个类的直接父类上，
甚至可以在没有直接父类中使用它。
"""
class A:
	def spam(self):
		print ("A.spam")
		super().spam()  # 寻找mro上一层的spam()方法

#a = A() 
#a.spam()# 'super' object has no attribute 'spam'

class B:
	def spam(self):
		print ("B.spam")

class C(A, B):
	pass

c = C()
c.spam()
"""
A.spam  
B.spam
"""
print (C.__mro__)
##->(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


"""
总结：
	首先确保继承体系中所有同名的方法都有可兼容的调用名称（参数类型，个数都相同）
		如果super() 尝试去调用非直接父类的方法，那么这就可以确保不会遇到麻烦
	
	其次确保最顶层的类实现了这个方法通常是一个好主意。
	沿着MRO列表展开的查询链会因为最终找到了实际的方法为止。


"""




























