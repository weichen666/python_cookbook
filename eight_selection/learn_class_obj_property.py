#/usr/bin/env python

class Person:
	def __init__(self, first_name):
		self.first_name = first_name

	#getter function
	@property
	def first_name(self):
		return self._first_name

	# setter function
	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str):
			raise TypeError('Excepted a string')
		self._first_name = value

	# delete function
	@first_name.deleter
	def first_name(self):
		raise AttributeError("Can't dlte attribute")

"""
除非属性通过@property的方式定义过了
否则不能定义@属性.setter和@属性.deleter
"""

a = Person("Guido")
print (a.first_name) # call ther getter
#a.first_name = 2 #->Excepted a string
a.first_name = "zhang"
print (a.first_name)

#del a.first_name #->Can't dlte attribute

"""
	当实现一个property时，
	底层的属性（如果有的话）仍然需要被保存到某个地方，
	因此get和set方法中，我们是直接对_first_name进行操作的，则就是属性实际保存的地方。
	在__init()中设置self.first_name是因为，在初始化的时候也会进行类型检查（调用setter方法）

"""

"""
在已经存在的get和set方法中定义property
"""
class Person:
	def __init__(self, first_name):
		self.set_first_name(first_name)

	def get_first_name(self):
		return self._first_name

	def set_first_name(self, value):
		if not isinstance(value, str):
			raise TypeError("excepted a string")
		self._first_name = value


	def del_first_name(self):
		raise AttributeError("Can't delete attribute")

	name = property(get_first_name, set_first_name, del_first_name)

"""
property 实际上就是把一系列方法绑定在一起。
property 底层绑定的方法
"""
print (Person.name.fget)
print (Person.name.fset)
print (Person.name.fdel)

"""
总结：
	(1)如果只是单纯的提供getter/setter的话，不用使用property属性
	(2)property可以使得接口便的非常统一 如:Circle类
	(3)不用重复性的property的代码。
"""

import math
class Circle:
	def __init__(self, radius):
		self.radius = radius

	@property
	def area(self):
		return math.pi * self.radius ** 2

	@property
	def diameter(self):
		return self.radius ** 2
	
	@property
	def perimeter(self):
		return 2 * math.pi * self.radius

c = Circle(4.0)
print (c.radius)
print (c.perimeter)
#c.perimeter = 2 # 没有setter























