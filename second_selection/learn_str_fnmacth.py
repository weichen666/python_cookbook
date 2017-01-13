#!/usr/bin/env python

from fnmatch import fnmatch, fnmatchcase

"""
fnmatch() 函数使用底层操作系统的大小写敏感规则
不同的系统是不一样的)来匹配模式。
"""

resval = fnmatch("foo.txt", "*.txt")
print (resval) #->True

resval = fnmatch("foo.txt", "?oo.txt")
print (resval) #->True

resval = fnmatch("Dat45.csv", "Dat[0-9]*")
print (resval) #->False

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
fl = [name for name in names if fnmatch(name, 'Dat*.csv')]
print (fl) #->['Dat1.csv', 'Dat2.csv']


#On OS X (Mac)
resval = fnmatch("foo.txt", "*.TXT")
print (resval) #->False

#(window)
resval = fnmatch("foo.txt", "*.TXT")
print (resval) #->True



"""
在处理非文件名的字符串也是很有用处
"""

addresses = [
	'5412 N CLARK ST',
	'1060 W ADDISON ST',
	'1039 W GRANVILLE AVE',
	'2122 N CLARK ST',
	'4802 N BROADWAY'
]

from fnmatch import fnmatch
resval = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print (resval) #->['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']