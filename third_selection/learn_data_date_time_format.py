#!/usr/bin/env python

x = 1234.56789

# two decimal places of accuracy
print (format(x, "0.2f")) #->1234.57

# 右对齐10个字符，一位精度
print (format(x, ">10.1f"))#->    1234.6

# 左对齐
print (format(x, "<10.1f"))#->1234.6    

#居中对齐
print (format(x, "^10.1f"))#->  1234.6  

# 千位插入, 
print (format(x, ","))#->1,234.56789
print (format(x, "+,.1f")) #->1,234.6

#科学计数法
print (format(x, "e")) #->1.234568e+03
print (format(x, "E")) #->1.234568E+03

"""
千分位支持,
"""
print(format(x, ",").translate({ord("."):",",ord(","):"."}))

"""
同时指定宽度和精度的一般格式：
[<>^]?width[,]?(.digits)?
适用于字符串的format()函数
"""

"""
使用% 格式化数字，有些功能不被支持了()
"""






