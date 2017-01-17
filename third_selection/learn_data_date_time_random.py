#!/usr/bin/env python

# random 模块

import random

values = [1, 2, 3, 4, 5, 6]

#取一个值
print (random.choice(values))
print (random.choice(values))

#取N个不同的元素作用样本
print (random.sample(values, 2))
print (random.sample(values, 3))

#打乱元素的顺序
random.shuffle(values)
print (values)

#随机生成一个整数
print (random.randint(0, 10))

#生成一个浮点数在0~1之间
print (random.random())

#获取N位随机数（二进制）的整数
print (random.getrandbits(2))


"""
修改random模块中的生成随机数的算法

	random.seed() 方法实现

"""