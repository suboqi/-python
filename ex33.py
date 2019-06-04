# -*- coding:utf-8 -*-
i = 0
numbers = []

while i < 6:
	print("At the top i is %d" % i)
	#list.append(obj),相当于在lists列表后加上obj
	numbers.append(i)

	i = i+1
	print("Numbers now:",numbers)
	print("At the bottom i is %d" % i)

print("The Numbers:")

for num in numbers:
	print(num)

