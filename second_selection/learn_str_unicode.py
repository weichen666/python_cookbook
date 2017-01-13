#!/usr/bin/env python

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1) #->Spicy Jalapeño
print(s2) #->Spicy Jalapeño
print(s1 == s2) #->False
print(len(s1)) #->14
print(len(s2)) #->15


"""
使用 unicodedata 模块 将文本标准化\

	第一个参数：	
		指定字符串标准化的方式
			NFC:字符应该是整体组成（可能的话，使用单一编码）
			NFD:字符应该分解多个组合字符表示



"""
import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print (t1 == t2) #->True

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print (t1 == t2) #->True


# 清除某些变音符
"""
combining() 可以测试一个字符是否为和音字符，

"""
resval = ''.join(c for c in t1 if not unicodedata.combining(c))
print(resval) #->Spicy Jalapeno