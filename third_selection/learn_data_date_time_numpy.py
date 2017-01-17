#!/usr/bin/env python

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)
#print(x + 10) 报错
print (x + y)

import numpy as np
ax = np.array(x)
ay = np.array(y)
print(ax * 2) #->[2 4 6 8] 2倍
print(ax + 10) #->[11 12 13 14]都+10
print(ax + ay) #->[ 6  8 10 12]两个相加
print(ax * ay) #->[ 5 12 21 32]两个相乘



