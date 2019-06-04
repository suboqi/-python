# -*- coding:utf-8 -*-
# !usr/bin/python3
cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return "Not founf."

# ok pay attention!
# 好的，注意！
#cities['_find'] = find_city

while True:
	print("State?(ENTER to quit)",end = '')
	state = input("> ")
	if not state : break
	city_found = find_city(cities,state)
	print(city_found)