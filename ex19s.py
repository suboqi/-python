# -*- coding:utf-8 -*-
#定义一个函数只接受两个参数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
#打印
	print("You have %d cheeses!" % cheese_count)
	print("You have %d boxes_of_crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
#在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符,\n代表换行
	print("Get a blanket.\n")
	

	
#1、我们可以直接给出函数值
print("We can just give the function numbers directly:")
#
cheese_and_crackers(20,30)



#2、或者我们直接使用脚本中的变量
print("OR,we can use variables from our script:")
#
amount_of_cheese = 10
amount_of_crackers = 50
#然后再脚本内输出
cheese_and_crackers(amount_of_cheese,amount_of_crackers)



#3、甚至我们可以在里面运行数学算法
print("We can even do math inside too:")
#
cheese_and_crackers(10+20,5+6)



#4、我们可以把变量和数学结合起来
print("And we can combine the two,variables and math:")

cheese_and_crackers(amount_of_cheese +100,
amount_of_crackers +1000)


#5、我们可以把直接给出函数值和使用脚本中的变量结合起来
amount_of_crackers = 11
cheese_and_crackers(20,amount_of_crackers)

#6、
amount_of_crackers = 20
cheese_and_crackers(33,amount_of_crackers +20)

#7、
amount_of_cheese=100
amount_of_crackers=200
cheese_and_crackers(amount_of_cheese +221,amount_of_crackers +231)

#8、
amount_of_cheese=50
amount_of_crackers=300
cheese_and_crackers(amount_of_cheese,amount_of_crackers-20)

#9、
amount_of_cheese=100
amount_of_crackers=200
cheese_and_crackers(amount_of_cheese -221,amount_of_crackers *3)

#10、
amount_of_cheese = 101
cheese_and_crackers(amount_of_cheese-50,20)
