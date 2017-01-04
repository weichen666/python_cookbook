#!/usr/bin/env/python
#cofing=utf-8

"""
operator.itemgetter(item)
operator.itemgetter(*items)
	这个函数会调用所传入的操作数的__getitem__()方法返回一个带有item的可调用对象

operator.attrgetter(attr)
operator.attrgetter(*attrs)
	返回一个带有操作数中的attr属性的可调用对象


"""
from operator import itemgetter, attrgetter

#待排序数据
rows = [
	{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_name = sorted(rows, key=itemgetter('fname'))
print (rows_by_name)
"""
[{'uid': 1004, 'fname': 'Big', 'lname': 'Jones'}, 
{'uid': 1003, 'fname': 'Brian', 'lname': 'Jones'}, 
{'uid': 1002, 'fname': 'David', 'lname': 'Beazley'}, 
{'uid': 1001, 'fname': 'John', 'lname': 'Cleese'}]
"""

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print (rows_by_uid)
"""
[{'lname': 'Cleese', 'fname': 'John', 'uid': 1001}, 
{'lname': 'Beazley', 'fname': 'David', 'uid': 1002}, 
{'lname': 'Jones', 'fname': 'Brian', 'uid': 1003}, 
{'lname': 'Jones', 'fname': 'Big', 'uid': 1004}]
"""

# 支持多个
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
"""
[{'uid': 1002, 'lname': 'Beazley', 'fname': 'David'}, 
{'uid': 1001, 'lname': 'Cleese', 'fname': 'John'}, 
{'uid': 1004, 'lname': 'Jones', 'fname': 'Big'}, 
{'uid': 1003, 'lname': 'Jones', 'fname': 'Brian'}]
"""


# 使用lambda 表达式替代
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key= lambda r: (r['lname'], r['fname']))
