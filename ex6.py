# -- coding: utf-8 --
#有10种类型的人
x = "There are %d types of people." %10#字符串包含字符串
#命名binary 二进制
binary = "binary"
#命名
do_not = "don't"
#有些人知道binary，有些人不知道binary
y = "Those who know %s and those who %s" %(binary,do_not)#字符串包含字符串
#打印x，y
print (x)
print (y)
#我说x
print("I  said:%r."%x)#字符串包含字符串
#我也说y
print("I also said:'%s'."%y)#字符串包含字符串
#定义一个hilarious为false1/
hilarious = False
#定义一个jke
joke_evaluation = "Isn't that joke so funny?! %r"
#输出joke
print(joke_evaluation % hilarious)
#两段话w e 
w = "This is the left side of..."
e = "a string with a right side"
#输出w+e
print(w+e)
/