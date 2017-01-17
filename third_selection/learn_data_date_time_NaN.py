#!/usr/bin/env python

a = float("inf") #->inf
b = float("-inf") #->-inf
c = float("nan") #->nan
print (a)
print (b)
print (c)

#测试这些值math模块下
import math
print (math.isinf(a))
print (math.isinf(b))
print (math.isnan(c))

# 无穷值满足数学中的运算
print (a + 45)
print (a * 10)
print (10/a)

# 未定义的并返回一个NaN结果
print (a / a)
print (a + b) 

# NaN 和其余值元素都是NaN
print (c / 2) 

#NaN自己与自己比较都是False（js语法）
d = float("nan")
print (c == d) #->False
print (c is d) #->False

#测试是否为nan的办法是math.isnan()
