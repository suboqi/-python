#!/usr/bin/env python3
# -*- coding:utf-8 -*-
n = 100
sum = 0
counter = 0
while counter <= n:
	sum = sum + counter
	counter += 1

print("1到 %d 之和为： %d " %(n,sum))

n = 100
sum = 0
counter = 1
while counter <= n:
	sum = sum + counter
	counter += 1

print("1到 %d 之和为： %d " %(n,sum))

n = 100
sum = 0
counter = 50
while counter <= n:
	sum = sum + counter
	counter += 1

print("1到 %d 之和为： %d \n" %(n,sum))
#实现无限循环
"""var = 1
while var == 1 : #表达式永远为true
num = int(input("输入一个数字："))
	print("你输入的数字是：",num)

print("Good bye!")"""

count = 0
while count < 5:
	print(count ,"小于5")
	count = count + 1
else:
	print(count,"大于或者等于5")
#这里flag为1，系统判定为True,所以程序不停循环
"""flag = 1
while(flag):print("欢迎来到菜鸟教程")
print("Good bye!")"""
#这里flag为0，系统判定为False,所以程序打印Good bye！
flag = 0
while(flag):print("欢迎来到菜鸟教程")
else:
	print("Good bye!\n")
#for-loop:
"""for <variable> in <sequence>:
    <statements>
else:
    <statements>"""
#for - break循环，break循环适用于跳出当前循环体
sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
	if site == "Runoob":
		print("菜鸟教程")
		break
	print("循环数据" + site)
#执行脚本后，在循环到 "Runoob"时会跳出循环体：
else:
	print("没有循环数据：")
print("完成循环！\n")
#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for letter in 'Runoob':#第一个实例
	if letter == 'b':
		break
	print("当前字母为：",letter)

var = 10
while var >0:
	print("当期变量值为：",var)
	var = var -1
	if var < 5:
		break

print("Good bye!\n")
#continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for letter in 'Runoob':#第一个实例
	if letter == "o":#当字母为0时跳过输出
		continue
	print('当前字母：',letter)

var = 10#第二个实例
while var > 0:
	var = var -1
	if var == 5:#当变量为5时跳过输出
		continue
	print('当前变量值：',var)
print("Good bye!\n")
#循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n,'等于',x,'*',n//x)
	else:
		#循环中没有找到元素
		print(n,'是质数')