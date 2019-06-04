# -*- coding:utf-8 -*-
people = 20
cats = 30
dogs = 15
#
if people < cats:
	print("Too many cats ! The world is doomed !")

if people > cats:
	print("Not many cats ! The world is saved !")

if people < dogs:
	print("The world is drooled on !")

if people > dogs:
	print("The world is dry")
#"+="加法赋值运算符，等价于“dogs = dogs + 5”
dogs += 5

if people >= dogs:
	print("People are greater than or equal to dogs ")

if people <= dogs:
	print("People are less than or equal to dogs")

if people == dogs:
	print("People are dogs.")