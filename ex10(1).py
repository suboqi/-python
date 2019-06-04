formatter = "\n%r \\%r %r \t%r"#%r 打印出来的是你写在脚本里的内容

print (formatter % (1,2,3,4))

print (formatter % ("one","two","three","four"))

print (formatter % (True,False,False,True))#首字母必须大写，不然报错

print (formatter % (formatter,formatter,formatter,formatter))

print (formatter % (

	" I had this thing.",
	" That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))

print("------")

formatter = "\n%s \\%s %s \t%s"#而 %s 打印的是你应该看到的内容

print (formatter % (1,2,3,4))

print (formatter % ("one","two","three","four"))

print (formatter % (True,False,False,True))#首字母必须大写，不然报错

print (formatter % (formatter,formatter,formatter,formatter))

print (formatter % (

	" I had this thing.",
	" That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))