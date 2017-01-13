#!/usr/bin/env

filename = 'spam.txt'

print (filename.endswith(".txt"))
print (filename.startswith('file:'))


# 如果想检测多个可能性，
#只需要将所有匹配项放入元组中，然后传递给startswith()或endswith()
# 必须传入一个tuple，list和set都不行
import os

# 获取当前目录下的所有文件
filenames = os.listdir(".")
f = (onefile for onefile in filenames if onefile.endswith((".c", ".h")))
print (list(f))


# 读取文件或者网络
from urllib.request import urlopen
def read_data(name):
	if name.startswith(("https:", "http:", "ftp:")):
		return urlopen(name).read()
	else:
		with oepn(name) as f:
			return f.read()

# 配置 数据聚合使用 (any , all)
if all(name.endswith(('.c', '.h')) for name in list(filenames)):
	print (True)
else:	
	print (False)