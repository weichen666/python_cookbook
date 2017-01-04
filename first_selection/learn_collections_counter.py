#!usr/bin/env python

from collections import Counter

# 定义一个列表
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

#生成Counter对象
word_counts = Counter(words)

#出现次数前三的元素
top_three = word_counts.most_common(3)
print (top_three)
"""
	[('eyes', 8), ('the', 5), ('look', 4)]
"""




print (word_counts['not'])

print (word_counts['eyes'])


# 手动新增
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
	word_counts[word] += 1

print (word_counts['eyes'])

# 使用更新方法
word_counts.update(morewords)
print (word_counts['eyes'])


# Counter 实例 	很容易跟数学运算操作结合

a = Counter(words)
b = Counter(morewords)

print (a)
print (b)

c = a + b
print (c)

d = a - b
print (d)

#Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具



# 创建Counter
c = Counter() # 创建空Counter类
print (c)
c = Counter("gallahad") # 从一个可iterable对象中创建(list, dict, str, set, tuple) 
print (c)
c = Counter({"a":4, "b":2}) #从一个字典中创建
c = Counter(a = 4, b = 2) # 从一个字典解析中创建

#计数值的访问与缺失的键
#当所访问的键不存在时，返回0，而不是KeyError；否则返回它的计数。
c = Counter("abcdefgab")
print (c["a"]) # -> 2
print (c["h"]) # -> 0

# 计数器的更新（update和subtract）+/-
#新增
c = Counter('which')  
c.update('witch')  # 接受一个可iterable对象
print (c['h']) # ->3
d = Counter("watch")
c.update(d) # 接受另一个Counter对象
print(c['h']) # ->4

#减少 
c = Counter("which")
c.subtract("witch") #接受一个可iterable对象
print (c["h"]) # ->1
d = Counter("watch")
c.subtract(d)
print (c['a']) # ->-1

#键的删除
#当计数值为0时，并不意味着元素被删除，删除元素应当使用del。
c = Counter("abcdcba")
c["b"] = 0
print (c) #->Counter({'c': 2, 'a': 2, 'd': 1, 'b': 0})
del c["a"]
print (c) #->Counter({'c': 2, 'd': 1, 'b': 0})

# elements() 值
#返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。
#所有元素按照字母序排序，个数小于1的元素不被包含。
c = Counter(a = 4, b =2, c = 0, d = -1)
for i in c.elements():
	print(i, end=' ') # ->a a a a b b 
print()


# most_common([n])
#返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，按照字母序排列。
c = Counter("abracadabra")
print (c.most_common()) #->[('a', 5), ('r', 2), ('b', 2), ('d', 1), ('c', 1)]
print (c.most_common(3))#->[('a', 5), ('b', 2), ('r', 2)]


# 浅拷贝
c = Counter("abcdcba")
print (id(c)) #-> 18681432
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
d = c.copy()
print (id(d)) #-> 18680472
print (d == c) #-> True

# 算术和集合操作
#+、-、&、|操作也可以用于Counter。其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。
#需要注意的是，得到的Counter对象将删除小于1的元素。

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print (c + d) #-> Counter({'a': 4, 'b': 3})
print (c - d) #-> Counter({'a': 2})
print (c & d) #交集: min(c[x], d[x]) -> Counter({'a': 1, 'b': 1})
print (c | d) #并集: max(c[x], d[x]) -> Counter({'a': 3, 'b': 2})

# 常用操作
c = Counter('abracadabra')
print (sum(c.values())) #所有计数的总数 -> 11
c.clear() # 重置Counter对象，注意不是删除
print (c) #-> Counter()

c = Counter('abracadabra')
print(list(c))# 将c中的键转为列表 -> ['r', 'd', 'c', 'a', 'b']

print(set(c)) # 将c中的键转为set -> {'b', 'r', 'c', 'd', 'a'}

print(dict(c))# 将c中的键值对转为字典 ->{'r': 2, 'c': 1, 'a': 5, 'd': 1, 'b': 2}

print(c.items())  # 转为(elem, cnt)格式的列表->dict_items([('c', 1), ('b', 2), ('r', 2), ('d', 1), ('a', 5)])

print(c.most_common()[:2:-1]) #  取出计数最少的2个元素 ->[('c', 1), ('d', 1)]

c['a'] = -1
print (c) #->Counter({'r': 2, 'b': 2, 'c': 1, 'd': 1, 'a': -1})
c += Counter() #  移除0和负值
print (c) #->Counter({'b': 2, 'r': 2, 'c': 1, 'd': 1})

