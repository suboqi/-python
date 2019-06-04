#!/usr/bin/env python
# -*- coding:utf-8 -*- 

file_abs = "D:\\python\\笨办法学python\\python读取文件\\ex15_sample.txt"

try:
	f = open(file_abs,"r")
	
	print(f.read())

finally:
	
	if f:
	
			f.close()