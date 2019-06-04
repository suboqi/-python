# -*- coding:utf-8 -*-
#让我们练习一下
print("Let's practice everything.")
#你需要知道制表符和换行符的转义，“\’”代表单引号，“\\”代表反斜杠，“\n”代表换行符，“\t”代表横向制表符，“\v”代表竖向制表符
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#定义一个poem，里面的内容是“”“.......""".三个“”“代表可以直接打印多行内容，并且用法和‘’‘没有区别
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none\
"""

#隔断
print("-----------------")
print(poem)
print("-----------------")

#定义一个简单的five，做运算，并打印出five
five = 10 - 2 + 3 - 6
print("This should be five: %s"%five)
#定义一个函数为：secret_formula，并进行相应的数学计算
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans ,jars,crates
#定义start_point，并将start_point赋值给started,started赋值给jelly_beans，jars，crates
start_point = 10000
beans,jars,crates = secret_formula(start_point)
#打印start_point，heans，jars，crates
print("With a starting point of: %d" % start_point)
print("We'd have %d beans,%d jars,and %d crates." %(beans,jars,crates))
#现在将start_point变量变化一下，从新使用函数运行
start_point = start_point / 10
#现在让我们实验另一种方法
print("We can also do that this way:")
print("We'd have %d beans, %d jars,and %d crates." % secret_formula(start_point))