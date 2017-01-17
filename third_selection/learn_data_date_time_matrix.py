#!/usr/bin/env python

import numpy as np

#创建矩阵
m = np.matrix([
[1, -2, 3],
[0, 4, 5],
[7, 8, -9]
])
print (m)

print (m.T)

print (m.I)

v = np.matrix([
[2],
[3],
[4]])

print (m * v)
