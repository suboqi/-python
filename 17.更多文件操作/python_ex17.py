#-*- coding:utf-8 -*-
#从sys中使用argv列表
from sys import argv
#从os.path模块中进行存在选择，存在为True，不存在为False
from os.path import exists
#argv接受列表变量
script,from_file,to_file=argv
#d打印Copying from test.txt to copied.txt ，记住转义符格式化不要把符号写错了
print("Copying from %s to %s" % (from_file,to_file))
#we could to these two on one line too，how？
#打开test.txt定义in_file
in_file = open(from_file)
#读取in_file定义indata
indata = in_file.read()
#Python len() 方法返回对象（字符、列表、元组等）长度或项目个数：用法：len(s),--s为对象
print("The input file is %d bytes long" % len(indata))
#exists判断文件夹是否存在
print("Does the output file exist? %r" % exists(to_file))
#打印
print("Readay,hit RETURN to continue,CTRL-C to abort.")

input()
#打开to_file只用于写入到out_file
out_file = open(to_file,'w')
#写入从上面从test.txt中读的内容
out_file.write(indata)
#打印
print("Alriht,all done")
#关闭out_file
out_file.close()
#关闭in_file
in_file.close()