#-*- coding:utf-8 -*-
#从sys中使用argv列表
from sys import argv
#获取参数，第一个为运行的脚本，第二个供脚本读取的参数（必须输入两个参数，不然报错）
scripr,filename = argv
#打印We're going to arase test.txt
print("We're going to arase %r." %filename)
#打印If you don't want that,hit CTRL-C(^C)
print("If you don't want that,hit CTRL-C(^C)")
#打印If you do want that,hit RETURN
print("If you do want that,hit RETURN")
#input作为一个中断程序执行的作用
input("?")
#打印Opening the file...
print("Opening the file...")
#记得这是一个小写的'w',不然报错，打开test.txt，并只应用于写入
#'r',只读打开文件，文件指针放在表头
#'r+',打开文件用于读写，指针放在文件开头
#'w+',打开文件用于读写，文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。如果该文件不存在，创建新文件。
#'a',打开一个文件用于追加。如文件存在，指针会放在文件结尾。新内容将被写入已有内容之后。如果该文件不存在，创建新文件进行写入
#'a+',打开一个文件用于读写。如文件存在，指针会放在文件结尾。新内容将被写入已有内容之后。如果该文件不存在，创建新文件进行写入
target = open(filename,'w')
#打印Truncating the file.Goodbye!
print("Truncating the file.Goodbye!")
#truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
target.truncate()
#打印Now I'm going to ask you for three lines
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")

line2 = input("line 2: ")

line3 = input("line 3: ")
#向文件内写入上面的三个句子
print("I'm going to write these to the file")

target.write('%s\n,%s\n,%s\n'%(line1,line2,line3))
#
print("And finally,we close it.")

target.close()