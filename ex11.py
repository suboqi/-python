# -*-coding:utf8-*-
#在print后面加上一个逗号，这样的话print就不会输出新行符而结束这一行到下一行了
print("How old are you ?"),

age = input()#个锤子，python3.0新特性，目前只有input()了，
#这里得注意，数字可以直接使用（），如果是文本得带上“”或者‘’，转换格式。
 
print("How tall are you?"),

height = input(" ")

print("How much do you weight?"),

weight = input()
#单引号需要被转义，从而防止它被识别为字符串的结尾。age=35,height=6'2",weight=180lbs
print("So, you're %r old, %r tall and %r heavy."%(
age,height,weight))