# 从sys中使用argv列表
from sys import argv
#获取参数，第一个为运行的脚本，第二个供脚本读取的参数
script,filename = argv
#打开ex15_simple.txt文本文件，并将它传给txt文件
txt = open(filename)
#打印
print("Here's your file %r:" %filename)
#打印
print(txt.read())
#打印
print("Type the filename again:")
#输出为file_again赋值
file_again = input(">")
#打开filename文本
txt_again = open(file_again)
#打印
print(txt_again.read())