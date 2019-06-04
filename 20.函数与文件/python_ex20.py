#-*- coing:utf-8 -*-
#
from sys import argv
#
script,input_file = argv
#新建print_all函数，里面有一个f参数
def print_all(f):
#这个函数执行f.read()
	print (f.read())
#新建一个rewind函数，里面有一个f参数
def rewind(f):
#seek() 方法用于移动文件读取指针到指定位置。
#seek() 方法语法如下：fileObject.seek(offset[, whence])
#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#whence：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
#f.seek(0)表示移动文件指针从头开始
	f.seek(0)
#定义一个print_a_line函数，里面有两个参数line_count,f
def print_a_line(line_count,f):
#执行line_count,freadline()
	print (line_count,f.readline())
#定义current_file，打开test.txt测试文件
current_file = open(input_file)
#首先让我们打印整个文件，记得换行符
print("First let's print the whole file:\n")
#打印读取到test.txt文件的内容
print_all(current_file)
#现在让我们倒带，这有点像磁带
print("Now let's rewind,kind of like a tape")
#定位当前位置
rewind(current_file)
#让我们打印这三行
print("Let's print three lines")
#打印文档第一行内容
current_line = 1
print_a_line(current_line,current_file)
#打印文档第二行内容
current_line = current_line + 1
print_a_line(current_line,current_file)
#打印文档第三行内容
current_line = current_line + 1
print_a_line(current_line,current_file)