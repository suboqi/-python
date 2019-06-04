def search_around1():
	print("\n这是一个游戏，需要依靠你的选择来完成")
	print("\n游戏数据只让输入'上'，'下'，'左'，'右'")
	print("\n开始游戏")
	print("\n请开始选择")
	
	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()
 
	elif next == "右":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n你得重新开始选择咯")
		search_p1()
 
	elif next == "上":
		print("\n恭喜你，走出了第一步，可以看到地图的一部分")
		origin_room_map1()

	else:
		print("你没有阅读游戏规则，请阅读后在重新开始")
		search_around1()

def origin_room_map1():
	print( """
	|=====================================================|
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|=======| |===============| |================| |======|
	|        2                 3                  4       |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	
	""")
	search_around2()

def search_around2():
	print("\n你面前有三扇门，编号为'2','3','4',请输入相应的编号")
	print("\n这三扇门属于前门，不需要钥匙，但是进入后门则需要钥匙")
	print("\n可以告诉你，每扇门内得到的钥匙，一定不能打开当前的后门")
	print("\n开始选择吧！")

	next = input("> ")

#这里犯了个错，"2","3","4"都是用的if函数，导致要把这三扇门都打开了才能返回，后来改成elif完美解决
	if next == "2" :
		print("\n准备好了吗？现在给你展示2号房间的部分地图")
		print("\n记住，游戏数据只让输入'上'，'下'，'左'，'右'")
		origin_room_map2()
		search_p1()

	elif next == "3" :
		print("\n准备好了吗？现在给你展示3号房间的部分地图")
		print("\n记住，游戏数据只让输入'上'，'下'，'左'，'右'")
		origin_room_map3()
		search_p2()

	elif next == "4" :
		print("\n准备好了吗？现在给你展示4号房间的部分地图")
		print("\n记住，游戏数据只让输入'上'，'下'，'左'，'右'")
		origin_room_map4()
		search_p3()

	else:
		print("\n系统不知道你在输入什么，请重新输入")
		search_around2()




def origin_room_map2():
	print( """
	|=====================================================|
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|=======|-|=======|                                   |
	|     |     |     |                                   |
	|     |     |     |                                   |
	|-----|-----|-----|                                   |
	|     |     |     |                                   |
	|     |     |     |                                   |
	|-----|-----|-----|                                   |
	|     |     |     |                                   |
	|     |     |     |                                   |
	|=======| |===============| |===============| |== ====|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	
	""")
#这里运行程序报错“python报错invalid character in identifier，意思就是“标识符中的无效字符”，检查下有没有字符是中文的，把中文字符改成英文字符再运行”
#if "左" in next or "右" in next:
def search_p1():

	next = input("> ")

	if next == "左":
		print("\n请继续选择")
		search_p1_p1()

	elif next == "右":
		print("\n请继续选择")
		search_p1_p2()

	elif next == "上":
		print("\n你离得到钥匙的机会又进了一步")
		print("\n请继续选择")
		search_p1_p3()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n你得重新开始选择咯")
		search_p1()

	else:
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p1_p1():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()

	elif next == "下":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "右":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n你得重新开始选择咯")
		search_p1_p1()

	else:
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p1_p2():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "右":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n你得重新开始选择咯")
		search_p1_p2()

	else:
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p1_p3():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者，你掉进陷阱死掉了,游戏结束")
		dead()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n你得重新开始选择咯")
		search_p1_p3()

	elif next == "上":
		search_p1_p3_p1()

	else:
		print("\n看样子你并没有阅读游戏规则，勇者，请再熟悉一遍！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p1_p3_p1():
		print("\n勇者，你离钥匙又近了一步")
		print("\n请输入关键的最后几步！！！")

		next = input("> ")

		if  next == "左":
			print("\n恭喜你，勇者，你拿到了宝箱的钥匙！！！")
			print("\n宝箱的钥匙，暗码为“312456897”")
			print("\n记住这串暗码，建议是你直接抄写下来")
			print("\n准备到map1重新选择")
			origin_room_map1()

		elif next == "上":
			print("\n这是7#房间前门被封住了，勇者，走另一条路吧！再选择一次")
			search_p1_p3_p1()

		elif next == "右":
			print("\n勇者，这条路是死胡同，我可以让你再选择一次")
			search_p1_p3_p1()

		elif next == "下":
			print("\n勇者，功亏一篑啊，你还是走了回头路！")
			dead()

		else:
			print("\n看样子你并没有阅读游戏规则，勇者，请再熟悉一遍！")
			print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
			search_around2()

def dead():
	print("\nGAME OVER!!!")


def origin_room_map3():
	print("""
	|=====================================================|
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                 |=================|                 |
	|                 |     |     |     |                 |
	|                 |     |     |     |                 |
	|                 |-----|-----|-----|                 |
	|                 |     |     |     |                 |
	|                 |     |     |     |                 |
	|                 |-----|-----|-----|                 |
	|                 |     |     |     |                 |
	|                 |     |     |     |                 |
	|=======| |=======|=======| |===============| |=======|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	""")

def search_p2():

	next = input("> ")

	if next == "左":
		print("\n请继续选择")
		search_p2_p1()

	elif next == "右":
		print("\n请继续选择")
		search_p2_p2()

	elif next == "上":
		print("\n恭喜你，勇者你掉进陷阱里面了，游戏结束！")
		dead()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p2_p1():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你离游戏又进了一步！")
		search_p2_p1_p1()

	elif next == "右":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p2_p2():

	next = input("> ")

	if next == "右":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你离游戏又进了一步！")
		search_p2_p2_p1()

	elif next == "左":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p2_p1_p1():
	
	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者，你掉进陷阱了，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你离游戏又进了一步！")
		last1()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p2_p2_p1():

	next = input("> ")

	if next == "右":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "左":
		print("\n恭喜你，勇者，你掉进陷阱了，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你离游戏又进了一步！")
		last2()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def last1():

	next = input("> ")

	if next == "上":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者，你拿到了宝箱的钥匙！！！")
		print("\n5#门的钥匙，暗码为“254689753”")
		print("\n记住这串暗码，建议是你直接抄写下来")
		print("\n准备到map1重新选择")
		origin_room_map1()

	elif next == "左":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def last2():

	next = input("> ")

	if next == "上":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "左":
		print("\n恭喜你，勇者，你拿到了宝箱的钥匙！！！")
		print("\n5#门的钥匙，暗码为“254689753”")
		print("\n记住这串暗码，建议是你直接抄写下来")
		print("\n准备到map1重新选择")
		origin_room_map1()

	elif next == "右":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def dead():
	print("\nGAME OVER!!!")


def origin_room_map4():
	print("""
	|=====================================================|
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                                     |
	|                                   |=======| |=======|
	|                                   |     |  5  |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|=======| |===============| |===============| |=======|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	""")

def search_p3():

	next = input("> ")

	if next  == "左" :
		print("\n恭喜你，勇者你掉进陷阱里面了，游戏结束！")
		dead()

	elif next  == "右" :
		print("\n请继续选择")
		search_p3_p1()

	elif next  == "上" :
		print("\n请继续选择")
		search_p3_p2()

	elif next  == "下" :
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，重新选择吧！")
		search_p1()
		
def search_p3_p1():

	next = input("> ")

	if next == "上":
		print("\n恭喜你，勇者你掉进陷阱里面了，游戏结束！")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "下":
		print("\n恭喜你，勇者，你走进死胡同，游戏结束！")
		dead()

	elif next == "左":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p3_p2():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者你掉进陷阱里面了，游戏结束！")
		dead()

	elif next == "右":
		print("\n恭喜你，勇者你掉进陷阱里面了，游戏结束！")
		dead()

	elif next == "上":
		print("\n恭喜你，勇者，你离游戏又进了一步！")
		last3()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def last3():

	next = input("> ")

	if next == "左":
		print("\n恭喜你，勇者，你拿到了7#钥匙！！！")
		print("\n7#门的钥匙，暗码为“235684951”")
		print("\n记住这串暗码，建议是你直接抄写下来")
		print("\n准备到map1重新选择")
		origin_room_map1()

	elif next == "右":
		print("\n勇者，这条路是死胡同，我可以让你再选择一次")
		last3()

	elif next == "上":
		print("\n恭喜你，勇者，你站在5#房间门口，输入正确的暗码才可以进入")
		come_in_room5()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def come_in_room5():

	print("\n请输入5#门对应的暗码！")

	next = input("> ")

	if next == "254689753":
		print("\n恭喜你进入了5#房间")
		origin_room_map5()

	else:
		chance1()

def chance1():
	print("\n现在给你三次机会")
	print("\n请输入吧！勇者")
	next = input("> ")

	if next == "254689753":
		print("\n恭喜你进入了5#房间")
		origin_room_map5()

	else:
		chance2()

def chance2():
	print("\n现在你只有两次机会了")
	print("\n请输入吧！勇者")
	next = input("> ")

	if next == "254689753":
		print("\n恭喜你进入了5#房间")
		origin_room_map5()

	else:
		chance3()

def chance3():
	print("\n现在你只有一次机会了")
	print("\n请输入吧！勇者")
	next = input("> ")

	if next == "254689753":
		print("\n恭喜你进入了5#房间")
		origin_room_map5()

	else:
		print("\n勇者，你并没有珍惜三次机会")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		dead()

def dead():
	print("\nGAME OVER!!!")


def origin_room_map5():
	print("\n勇者，恭喜你，现在给你一个小提示")
	print("\n你必须拿到宝藏钥匙，5#钥匙和7#钥匙，输入相应的暗码")
	print("\n记住，游戏数据只让输入'上'，'下'，'左'，'右'")
	print("\n现在给你展示4#房间和5#房间的地图")
	print("""
	|=====================================================|
	|                                   |     |     |     |
	|                                   |  1  |  2  |  3  |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |  4  |  5  |  6  |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |  7  |  8  |  9  |
	|                                   |=======| |=======|
	|                                   |     |  5  |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|=======| |===============| |===============| |=======|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	""")
	search_p4()

def search_p4():

	next = input("> ")

	if next == "左":
		print("\n你现在在7#位")
		print("\n在你面前有一根蜡烛")
		print("\n你面前有两个选择")
		print("\n点燃它,或者无视他")
		search_p4_p1()

	elif next == "右":
		print("\n你现在在9#位")
		print("\n在你面前有一根蜡烛")
		print("\n你面前有两个选择")
		print("\n点燃它,或者无视他")
		search_p4_p2()

	elif next == "上":
		print("被神选照的勇者啊，你还需要点亮前进的道路，才能拿到神之杖")
		print("请回去从新选择吧！")
		search_p4()

	elif next == "下":
		print("\n走错路了，勇者，英雄是不能回头的，加油！")
		print("\n给你一个惩罚，你从最开始的地方开始选择吧！勇者")
		search_around2()

	else:
		print("\n给你一个惩罚，你并没有阅读游戏规则，你从最开始的地方开始选择吧！勇者")
		search_around2()

def search_p4_p1():
	print("\n你现在在7#位")
	next = input("> ")

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到1#位，继续选择")
		search_p4_p1_p1()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p1()

def search_p4_p1_p1():

	print("\n你现在在1#位")

	next = input("> ")	


	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到3#位，继续选择")
		search_p4_p1_1()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p2()

def search_p4_p1_1():

	print("\n你现在在3#位")

	next = input("> ")	

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到9#位，继续选择")
		search_p4_p1_2()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p1_1()

def search_p4_p1_2():

	print("\n你现在在9#位")

	next = input("> ")	

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你解开了五星光芒的钥匙，5#位祭坛出现神之杖")
		print("\n神之杖暗码为“987654123”")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p1_1()



def search_p4_p2():

	print("\n你现在在9#位")
	next = input("> ")

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到3#位，继续选择")
		search_p4_p2_p1()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")

def search_p4_p2_p1():

	print("\n你现在在3#位")

	next = input("> ")	

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到1#位，继续选择")
		search_p4_p2_1()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p2()

def search_p4_p2_1():

	print("\n你现在在1#位")

	next = input("> ")	

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你马上跳转到7#位，继续选择")
		search_p4_p2_2()


	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p1_1()

def search_p4_p2_2():

	print("\n你现在在7#位")

	next = input("> ")	

	if next == "点燃它":
		print("\n恭喜你，勇者，你照亮了前进的道路")
		print("\n你解开了五星光芒的钥匙，5#位祭坛出现神之杖")
		print("\n神之杖暗码为“987654123”")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	elif next == "无视他":
		print("\n勇者，你没有照亮前进的道路")
		print("\n你得直面大魔王，加油，勇者，打败他！！！")
		room_evil()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		search_p4_p2_2()


def origin_room_map6():
	print("\n勇者，恭喜你，现在给你一个小提示")
	print("\n你必须拿到宝藏钥匙和7#钥匙，输入相应的暗码")
	print("\n现在给你展示5#房间和Evil房间的地图")
	print("""
	|=====================================================|
	|                 |     |     |     |     |     |     |
	|                 |     |     |     |  1  |  2  |  3  |
	|                 |-----|-----|-----|-----|-----|-----|
	|                 _     |     |     _     |     |     |
	|                 _Evil |     |     _  4  |  5  |  6  |
	|                 |-----|-----|-----|-----|-----|-----|
	|                 |     |     |     |     |     |     |
	|                 |     |     |     |  7  |  8  |  9  |
	|                 |=======| |=======|=======| |=======|
	|                                   |     |  5  |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|=======| |===============| |===============| |=======|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	""")

def room_evil():
	print("\n现在给你展示Evil房间的地图")
	origin_room_map6()
	print("\n你现在正在直面恶魔")
	print("\n请输入神之杖力量")

	next = input("> ")

	if next == "987654123":
		print("\n发动神之杖力量，打败魔王")
		print("\n恭喜你，勇者")
		print("\n你现在站在7#门的门口")
		come_in_room7()

	else:
		print("\n你被大魔王打败，游戏结束")
		dead()

def come_in_room7():
	print("\n请输入7#门的暗码")

	next = input("> ")

	if next == "235684951":
		print("\n恭喜你，勇者，你现在在在7#房间内")
		room7()

	else:
		print("\n我并不知道你输入了什么！！！请阅读游戏规则后在输入")
		come_in_room7()

def origin_room_map7():
	print("\n勇者，恭喜你，现在给你一个小提示")
	print("\n你必须拿到宝藏钥匙和输入相应的暗码")
	print("\n现在给你展示5#房间，宝藏房间和Evil房间的地图")
	print("""
	|=====================================================|
	|     |     |     |     |     |     |     |     |     |
	|  1  |  2  |  3  |     |     |     |     |     |     |
	|-----_-----|-----_-----|-----|-----_-----|-----|-----|
	|      Money|           |     |           |     |     |
	|  4  _  5  |  6  _Evil |     |     _     |     |     |
	|-----|-----|-----|-----|-----|-----|-----|-----|-----|
	|     |     |     |     |     |     |     |     |     |
	|  7  |  8  |  9  |     |     |     |     |     |     |
	|=======| |=======|=======| |=======|=======| |=======|
	|                                   |     |  5  |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|                                   |-----|-----|-----|
	|                                   |     |     |     |
	|                                   |     |     |     |
	|=======| |===============| |===============| |=======|
	|        2                 3                 4        |
	|                                                     |
	|                         YOU                         |
	|=======================||   ||=======================|
	""")

def room7():
	print("\n接下来让你更快的拿到宝藏")
	print("\n宝藏在5#位置，你现在直接跳转到4#位置")
	print("\n请输入宝藏房间的暗码")
	next = input("> ")

	if next == "312456897":
		print("恭喜你，勇者，你打开了宝箱")
		print("你拿到了宝藏")

	else:
		print("看样子你还没有拿到宝箱的钥匙，去2#房间吧，钥匙在那里")
		search_around1()

search_around1()


