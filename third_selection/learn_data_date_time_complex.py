#!/usr/bin/env python

a = complex(2, 4)
b = 3 -5j
print (a) #->(2+4j)
print (b) #->(3-5j)	

#属性
print (a.real) #->2.0
print (a.imag) #->4.0

#共轭
print (a.conjugate())#->(2-4j)

#+,-,*,/
print (a + b)#->(5-1j)
print (a - b)#->(-1+9j)
print (a * b)#->(26+2j)
print (a / b)#->(-0.4117647058823529+0.6470588235294118j)

#绝对值
print (abs(a))#->4.47213595499958

#正弦，余弦，正切 cmath包下(math包下面不支持复数)
import cmath
a = cmath.sqrt(-1)
print (a) #->1j






