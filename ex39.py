# -*- coding:utf-8 -*-
# 定义一个ten_things
ten_things = "Apple Oranges Crows Telephone Light Sugar"
#打印“等等，这里没有10件事物”
print("Wait there's not 10 things in that list,let's fix that.")
#split()通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
#split()方法语法：str.split(str="", num=string.count(str))
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
#num -- 分割次数。默认为 -1, 即分隔所有
stuff = ten_things.split(" ")
#stuff = ("Apple","Oranges","Crows","Telephone","LIght","Suger")
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
#判断stuff的长度是否不等于10个
while len(stuff) != 10:
	#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
	#pop()方法语法：list.pop([index=-1])
	#index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
	
	next_one = more_stuff.pop()
	print("Adding:",next_one)
	#next_one = "Boy"
	#append() 方法用于在列表末尾添加新的对象。
	#append()方法语法：list.append(obj)
	#obj -- 添加到列表末尾的对象。
	#这里应该是往stuff增加量，为"Boy","Girl","Banana","Corn"
	stuff.append(next_one)
	print("There's %d items now." % len (stuff))
	#print("There's 10 items now." )


print("There we go:",stuff)
#There we go:"Apple","Oranges","Crows","Telephone","Light","Suger","Boy","Girl","Banana","Corn"
print("Let's do some things with stuff.")

#print(stuff[]),语法报错
print(stuff[0])
#Apple
print(stuff[1])
#"Oranges"
print(stuff[-1])#whoa!fancy
#"corn"
print(stuff.pop())
#"Corn"
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#join()方法语法：str.join(sequence)
#sequence -- 要连接的元素序列。
print(''.join(stuff))#what?cool!
#Apple Orange Crows Telephone Light Suger Boy Girl Banana 
#stuff[3:5]
print('#'.join(stuff[3:5]))#super stellar!
#Crows#Telephone