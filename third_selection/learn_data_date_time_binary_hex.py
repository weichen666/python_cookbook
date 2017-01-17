#!/usr/bin/env python

x = 1234
print(bin(x))#->0b10011010010
print(oct(x))#->0o2322
print(hex(x))#->0x4d2

"""
不想输入0b,0o,0x 前缀
"""
print(format(x, 'b'))#->10011010010
print(format(x, 'o'))#->2322
print(format(x, 'x'))#->4d2

"""
整数符号位
"""
x = -1234
print(format(x, 'b'))#->-10011010010
print(format(x, 'o'))#->-2322
print(format(x, 'x'))#->-4d2



# 显示32位格式的
print(format(x + 2**32, 'b'))#->11111111111111111111101100101110
print(format(x + 2**32, 'o'))#->37777775456
print(format(x + 2**32, 'x'))#->fffffb2e


# 将不同进制转换为十进制整数

print(int('4d2', 16)) #->1234
print(int('10011010010', 2))#->1234


"""
Python 中的八进制是以 0o前缀的
"""