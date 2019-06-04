# -*- coding:utf-8 -*-
#!/usr/bin/python3
str = "This is string example......wow!!!"
print(str.split( ))  #以空格为分隔符
print(str.split('i',1))  #以i为分隔符
print(str.split('w'))  #以w为分隔符

txt = "google#Runoob#Taobao#Facebook"
#第二个参数为1，返回两个参数列表
x = txt.split("#",1)
print(x)

txt1 = "google#Runoob#Taobao#Facebook"
y = txt1.split("#",2)
print(y)