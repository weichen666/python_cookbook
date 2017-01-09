#!/usr/bin/env python

myTuple = (123, 'xyz', 45.67)

i = iter(myTuple)

print (next(i))
print (next(i))
print (next(i))
#print (next(i))  #->StopIteration

for i in iter(myTuple):
	print (i)


#遍历字典
kegends = {
	("a", "b"):(1809,1849),
	("c", "d"):(1852,1906)
}
# 遍历的是Key
for eachLegend in kegends:
	print ("Name:%s\tOccupation:%s" % eachLegend)

#遍历文件
myFile = open('iter_txt.txt', 'r') 

for line in myFile:
	print(line, end='')
print()


#自定义对象
class AnyIter(object):
	def __init__(self, data, safe=False):
		self.safe = safe
		self.iter = iter(data)

	def __iter__(self):
		return self
	def __next__(self, count=1):
		retval = []
		for item in range(count):
			try:
				retval.append(next(self.iter))
			except StopIteration:
				if self.safe:
					break
				else:
					raise
		return retval

a = AnyIter(range(10), True)
b = iter(a)
print (next(b))