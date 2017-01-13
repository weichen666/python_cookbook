#!/usr/bin/env python

"""
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
"""

"""
string 对象split() 
	它并不允许有多个分割符或者分割周围不确定的空格

re.split()
	灵活
"""

import re

line = "asdf fjdk; afed, fjek,asdf, foo"
resval = re.split(r'[;,\s]\s*', line)
print (resval) #->['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 使用括号分组(会保留分割的字符串)
resval = re.split(r'(;|,|\s)\s*', line)
print (resval)
#->['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


# 如果不想保留分割字符串在结果列表中，但是需要使用括号来进行分组
# 确保分组时非捕获分组的话,使用(?:...)

resval = re.split(r'(?:,|;|\s)\s*', line)
print (resval) #->['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']