#通过arvg进行批量参数赋值
from sys import argv

script,user_name = argv

prompt = '>'

print("Hi %s ,I'm the %s script." %(user_name,script))

print("I'd like to ask you a few questions.")


print("Do you like me %s?" %user_name)

likes = input(prompt)


print("Where do you live %s?"%user_name)

lives = input(prompt)


print("What kind of computer do you have?")

computer = input(prompt)


print("What do you favourite subject?")

subject = input(prompt)

print("""

Alright,so you said %r about liking me.

you live in %r. Not sure where that is.

And you have a %r computer .nice.

"""%(likes,lives,computer))

print('''

Alright,so you said %r about liking me.

you live in %r. Not sure where that is.

And you have a %r computer .nice.

'''%(likes,lives,computer))