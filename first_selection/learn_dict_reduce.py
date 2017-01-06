#!/usr/bin/env python
#coding=utf-8

prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB': 10.75
}

p1 = {key : value for key, value in prices.items() if value > 200}
print(p1) #->{'IBM': 205.55, 'AAPL': 612.78}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
print(type(tech_names)) # <class 'set'>

p2 = {key : value for key, value in prices.items() if key in tech_names}
print (p2) #{'IBM': 205.55, 'HPQ': 37.2, 'AAPL': 612.78}


# 创建元组序列(比较慢)
dict((key, value) for key, value in prices.items() if value > 200)