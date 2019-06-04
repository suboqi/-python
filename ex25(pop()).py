# -*- coding:utf-8 -*-
#
list1 = ['Google','Taobao','Jingdong','Tianmao']

print(list1[0:3])
print(list1[0:2])
print(list1[0:1])
print(list1[1:3])
print(list1[2:3])
print(list1[1:2])

list_pop = list1.pop(1)
list_pop1 = list1.pop(2)
print ("删除的项为：",list_pop)
print ("删除的项为：",list_pop1)
print ("列表现在为：",list1)
