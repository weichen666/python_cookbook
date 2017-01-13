#!/usr/bin/env python

import re

comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'

resval = comment.findall(text1)
print(resval)

text2 = """/* this is a
multiline comment */
"""
#匹配不到
resval = comment.findall(text2)
print(resval)


#1. 修改匹配方式

"""
(?:xxx) 指定了一个非捕获组。
	也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或编号的组
"""
comment = re.compile(r"/\*((?:.|\n)*?)\*/")
resval = comment.findall(text2)
print(resval) #->[' this is a\nmultiline comment ']

# 2.添加re.DOTALL 忽略
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
resval = comment.findall(text2)
print(resval) #->[' this is a\nmultiline comment ']