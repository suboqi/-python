# -*- coding:utf-8 -*-
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
#this first kind of for-loop goes through a list
#第一种for循环通过一个列表
for number in the_count:
	print("This is count %d" % number)
#same as above
#同上
for fruit in fruits:
	print("A fruit of type:%s" %fruit)

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it 
#我们也可以通过混合列表
#请注意我们必须使用％r，因为我们不知道它是什么
for i in change:
	print("I got %r" % i)

#we can also build lists,first atart with an empty one
#我们也可以建立列表，首先从空的列表开始
elements = []
#then use the range function to do 0 to 5counts
#然后使用范围函数执行0到5次计数
for i in range(0,6):
	print("Adding %d to the list." % i)

	#append is a function that lists understand
	#append是一个列出理解的函数
	elements.append(i)
	#append() 方法用于在列表末尾添加新的对象。
	#append()方法语法：list.append(obj)
	alist = [123,'abc','xyz','zara']
	alist.append(2009)
	print("new alist:",alist)

#now we can print them out too
#现在我们也可以打印出来
for i in elements:
	print("Element was: %d" % i)