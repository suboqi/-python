#使用%r，只有在想要获取某些东西的 debug 信息时才能用到 %r
formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))

print (formatter % ("one","two","three","four"))

print (formatter % (True,False,False,True))#首字母必须大写，不然报错

print (formatter % (formatter,formatter,formatter,formatter))

print (formatter % (

	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))

print ("__________________________")
#使用%s
formatter = "%s %s %s %s"
 
print (formatter % (1 , 2 , 3 , 4))

print (formatter % ("one" , "two" , "three" , "four"))

print (formatter % (True , False , False , True))

print (formatter % (formatter , formatter , formatter , formatter))

print (formatter % (
    "I had this thing.",
    "That you could type up rihgt.",
    "But it didn't sing.",
    "So I said goodnight."
))