
#!usr/bin/python
# -*-coding:utf-8-*-
 
from sys import argv
from os.path import exists
 
script , from_file , to_file = argv
# 定义值 script=lx0017.py  from_file=test.txt  to_file=copied.txt
 
print ("Copting from %s to %s" % (from_file , to_file))
# 打印   Copying from test.txt to copied.txt
 
in_file = open(from_file)
# 打开from_file定义in+file  
indata = in_file.read()
# 读取in_file定义indata 
 
print ("The input file is %d bytes long" % len(indata))
# 打印indata字符数
 
print ("Does the output file exist? %r" % exists(to_file))
# exists判断文件和文件夹是否存在
 
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
# 打印 Ready, hit RETURN to continue, CTRL-C to abort.
 
input()
 
out_file = open(to_file , "w")
#  以写模式 打开copied.txt
#  w代表写模式打开文件
#  r代表读模式打开文件
#  wr代表读写模式打开文件
#  w+代表读写模式打开文件
#  r+代表读写模式打开文件
#  a+代表读写模式打开文件
out_file.write(indata)
# 打开out_file写入indata
 
print ("Alriht , all done.")
# 打印
 
out_file.close()
# 关闭out_file
in_file.close()
