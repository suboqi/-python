# -*- coding:utf-8 -*-
def test_while(test_num):
	i = 0
	numbers = []

	while i < test_num :
		print("At the top i is %d" % i)
		numbers.append(i)
		i= i + 1
		print("Numbers now:",numbers)
		print("At the botton i is %d" %i)

	print("The numbers:")

	for num in nunbers:
			print(num)

test_while(7)