#-*- coding:utf-8 -*-
#this one is like your scripts with argv
#定义一个函数接受两个参数
def print_two(*args):

	arg1,arg2 = args
#将它们打印出来
	print("arg1:%r,arg2:%r" % (arg1,arg2))
#ok,thst *args is actually pointless,we can juet do this
#再次定义一个函数接受两个参数
def print_two_again(arg1,arg2):
#将它们打印出来
	print("arg1:%r,arg2:%r" % (arg1,arg2))
#this just takes one argument
#定义一个函数只接受一个参数
def print_one(arg1):
#将它们打印出来
	print("arg1:%s" % arg1)
#this one takes no arguments
#定义一个函数不接受任何参数
def print_none():
	print("I got nothin'.")

#输出
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


