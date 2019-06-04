# -*- coding"utf-8 -*-
#打开文件
fo = open("runoob.txt","r+")
print("文件名为: ",fo.name)
#
line = fo.readline()
print("读取的数据为：%s" % (line))
#
fo.seek(0,0)
line = fo.readline()
print("读取的数据为:%s" % (line))
#关闭文件
fo.close()