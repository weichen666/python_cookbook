#!/usr/bin/env python

# slice 在Python的应用
#截取某些部分
r = range(10)
print (list(r[ :5])) #  r[a:b]==> r[a, b).

#截取未知长度的列表
r[-1]
r[1:-1]
r[2:-2]

#在Python中，切片访问时，如果超出了数组的长度范围，只返回遍历到的元素

#只要开始位置
r[1:]
r[:] #复制

#步长
"""
如果步长为正数，则取元素的集合里表示从左到右的取值
如果步长为负数，则取元素的集合里表示从右到左的取值
"""

#slice 函数 slice( [start,] stop[, step]) 
""" 
返回一个切片对象，它表示的是range(start, stop, step)指定的范围。
start和step参数默认为None。切片对象有只读数据属性start，stop和step，它只是返回参数值（或默认）。没有其他明确的功能，但它们的作为数值Python和其他第三方扩展使用。
当使用扩展索引语法时也产生切片对象。
"""
## 返回一个切片对象
s = slice(5)
print (s.start)
print (s.step)
print (s.stop) 