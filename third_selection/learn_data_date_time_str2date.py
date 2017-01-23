#!/usr/bin/env python

from datetime import datetime

"""
格式说明:
	%Y: 4位年
	%m: 月份

strptime: 使用纯粹的Python实现
可以使用别的方式

"""
text = "2017-01-23"
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print (diff)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print (nice_z)


from datetime import datetime

def parse_ymd(s):
	y, m, d = s.split('-')
	return datetime(int(y),int(m), int(d))