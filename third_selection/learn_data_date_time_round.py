#!/usr/bin/env python

# 使用内置函数 round(value, ndigits)

"""
当一个值刚好在两边边界的中间时，
round() 函数返回离它最近的偶数
round(1.5) == round(2.5)  == 2
"""

print (round(1.23, 1)) #->1.2
print (round(1.27, 1)) #->1.3
print (round(1.5)) #->2
print (round(2.5)) #->2


"""
传递给round() 可以为负数: 舍入运算作用域十位，百位....
"""
print (round(154784, -2)) #->154800


"""
如果目的只是简单的输出一定的宽度，不要使用round()函数
格式化操作
"""
x = 1.296
print (round(x, 2)) #->1.3
print (format(x, '0.2f')) #->1.30
print ("value is {0:0.3f}".format(x)) #->value is 1.296

"""
不要使用 round() 来修正运算结果
"""
a = 2.1
b = 4.2
c = a + b
print (c) #->6.300000000000001
print (round(c, 2)) #-> 不推荐使用 

"""
使用decimal 模块解决午误差问题
"""

