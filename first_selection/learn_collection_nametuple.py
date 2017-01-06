#!/usr/bin/env python
#coding=utf-8

# 支持所有普通元组的操作，比如索引和解压
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber("xxx@xxx.com", '2017-01-05')
print (sub) #->Subscriber(addr='xxx@xxx.com', joined='2017-01-05')
print (sub.addr)  #->xxx@xxx.com
print (sub.joined) #->2017-01-05

#索引
print (sub[0]) #->xxx@xxx.com
#解压
addr, joined = sub
print(joined) #->2017-01-05


#用途（数据库中替代，如果数量巨大的话，比字典结构还有高效，但是命名元组是不可以更改的）
sub[0] = 'wsx@xx.com' #->异常 'Subscriber' object does not support item assignment

#如果非要修改的话，可以使用_replace() 方法，它会创建一个全新的命名元组并用新值取代
s = sub._replace(addr='wsx@xx.com')
print (s) #->Subscriber(addr='wsx@xx.com', joined='2017-01-05')


