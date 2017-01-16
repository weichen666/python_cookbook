#/usr/bin/env python

class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#交互界面打印(通常可以用它返回的字符串文本来重新创建这个实例)
	# 满足 obj = eval(repr(obj))
	def __repr__(self):
		return "Pair({0.x!r}, {0.y!r})".format(self)

	#str(), pring() 使用
	def __str__(self):
		return "({0.x!r}, {0.y!r})".format(self)

"""
!r：
 	应该使用__repr__()输出，而不是默认的__str__()输出
"""
p = Pair(3, 4)
print ("p is {0!r}".format(p))#->p is Pair(3, 4)
print ("p is {0}".format(p)) #->p is (3, 4)


"""
1. 对于__repr__() 标准做法是让它产生的字符串能够满足eval(repr(x)) == x

2. {0.x} :
	指代参数0的x属性，0实际上就代表实例self
	类似于:
		"Pair(%r, %r)" % (self.x, self.y)
"""