
from sys import argv
#获取参数，给script赋值python_ex15.py,给filename赋值ex15_simple.txt
script,filename = argv
#打开ex15_simple.txt文本文件
txt = open(filename)
#打印
print("Here's your file %r:" %filename)
#打印
print(txt.read())