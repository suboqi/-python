# -*-coding:utf-8-*-
 
 
from sys import argv
 
script , input_file = argv
 
def print_all(f):
	print (f.read())
#新建print_all函数 定义print (f.read())为函数代码
def rewind(f):
	f.seek(0)
#新建rewind函数 定义f.seek(0)为函数代码
def print_a_line(line_count,f):
	print (line_count , f.readline())
#新建print_a_line函数 定义print (line_count , f.readline())为函数代码
current_file = open(input_file)
#定义变量current_file 打开txt文档
print ("First let's print the whole file:\n")
#打印First let's print the whole file:
print_all(current_file)
#打印读取后的txt文档内容
print ("Now let's rewind, kind of like a tape.")
#打印Now let's rewind, kind of like a tape.
rewind(current_file)
#定位当前位置
print ("Let's print three lines:")
#打印Let's print three lines:
current_line = 1
print_a_line(current_line,current_file)
#打印文档第一排内容
current_line = current_line + 1
print_a_line(current_line,current_file)
#打印文档第二排内容
current_line = current_line + 1
print_a_line(current_line,current_file)
#打印文档第三排内容
