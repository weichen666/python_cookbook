#!/usr/bin/env python

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print (a + b)
print (a * b)

# 分母
print (a.numerator)
#分子
print (a.denominator)

# Converting to a float
print (float(a))

# float to Converting
x = 3.75
print(x.as_integer_ratio()) #->(15, 4)
y = Fraction(*x.as_integer_ratio())
print (y)#->15/4