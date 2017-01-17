#!/usr/bin/env pthon

from decimal import Decimal

"""
Decimal 接受字符串来表示数字, 
一般用于金融领域
"""
a = Decimal("4.2")
b = Decimal("2.1")
c = a + b
print (c) #->6.3


"""
Decimal 允许控制计算的每一个方面，
包括数字位数和四舍五入运算
"""

from decimal import localcontext
from decimal import Decimal
a = Decimal("1.3")
b = Decimal("1.7")
print (a / b) #->0.7647058823529411764705882353
with localcontext() as ctx:
	ctx.prec = 3
	print (a / b) #->0.765

