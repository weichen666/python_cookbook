#!/usr/bin/env python

class Student(object):
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age

	def __repr__(self):
		return repr((self.name, self.grade, self.age))


students = [
	Student('jane', 'B', 12),
    Student('john', 'A', 12),
    Student('dave', 'B', 10)
]

from operator import attrgetter

# 使用age进行排序 
print (sorted(students, key=attrgetter('age')))
#->[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 12)]

print (sorted(students, key=lambda x: x.age))

