#!/usr/bin/env python

a = {'x': 1, 'z' : 3}
b = {'y': 2, 'z' : 4}

from collections import ChainMap

"""
chainMap 接受多个字典并将它们在逻辑上变成一个字典。
然后，这些字典并不是真的合并在一起了。
ChainMap类只是在内部创建了一个容纳这些字典的列表
并重新定义了一些常见的字典操作来遍历这个列表。

如果出现重复键，那么第一次出现的映射值会被返回。

"""
c = ChainMap(a, b)

print (len(c)) # 3个key

print (list(c.keys()))

print (list(c.values()))

"""
如果要删除一个键, 则这个键必须出现在第一个map中
"""
# del c['y'] 报错
print (list(c.keys()))

#创建一个空Map
values = ChainMap()
values['x'] = 1
print (values) #->ChainMap({'x': 1})


"""
ChainMap 对于编程语言中的作用范围变量(比如 globals , locals 等)
是非常有用的
"""
#创建一个新的空Map
#将之前的ChainMap放在新建的列表后面
values = values.new_child()
values['x'] = 2
print (values) #->ChainMap({'x': 2}, {'x': 1})
values = values.new_child()
values['x'] = 3
print (values) #->ChainMap({'x': 3}, {'x': 2}, {'x': 1})

print(list(values.values())) #-> 3 

values = values.parents
print (values) #->ChainMap({'x': 2}, {'x': 1})

"""
update() 作为替代品
它需要你创建一个完全不同的字典对象(或者是破坏现有字典结
构)。 同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去
"""
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
b.update(a) #{'z': 3, 'y': 2, 'x': 1}
# 改变了b的结构
print (b)
a['x'] = 11
# 对a的修改不会映射到b上
print(b)




