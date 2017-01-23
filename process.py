#!usr/bin/env python
# coding=utf-8

import re
import random

str = """HQ3C3000008141
1
1
HM.HX2EE.001
Distributor
HM.HX2EE.001
End User
ACER LIQUID Z6 PLUS, DUAL SIM, 3GB/32GB, EU PLUG, GRAY, CENTRAL EU, SOUTH EU, EE, RU, UA
400
2017-01-23
HUAQIN
HUAQIN
HUAQIN
2
Manufacturer
Shanghai Pudong keyuan Road 399


Domain

Dongguan, CN
CN
201203
SHA
1
USD
112.69
20170123103628
20170123103628
EA
0
AAFgaNAHLAACZM/AAI

"""
a = re.split("\n", str)
print (len(a))

str_all = ""
for i in a:
	str_all += i


print(re.match("[a-zA-Z0-9@_\/\-,: \.]*", str_all).group())
