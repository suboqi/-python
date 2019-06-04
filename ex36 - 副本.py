def search_around1():
	print( "1.Climbe out the hole.")
	print( "2.Wait for the great devil come to kill you.")
	next = input("> ")
	if next == "1":
		try_again()
		search_around2()
	elif next == "2":
		dead()
	else:
		unknow_input()
		search_around1()
 
def search_around2():
	print( "1.Climbe out the hole.")
	print( "2.Wait for the great devil come to kill you.")
	next = input("> ")
	if next == "1":
		print( "Good job!You are now out of the deep hole.")
		search_around3()
	elif next == "2":
		dead()
	else:
		unknow_input()
		search_around2()
 
def search_around3():
	hint1()
	next = input("> ")
	if next == "1":
		print( "Oh,shit!You falled into a deep hole!")
		search_around1()
	elif next == "2":
		origi_room()
	else:
		unknow_input()
		search_around3()
 
def dead():
	print( "Sorry, this mission fails and you'll die soon.")
	exit(0)
		
def try_again():
	print( "Sorry, try again. It seems difficult for you."
	)
def unknow_input():
	print( "Sorry, I don't know what you want to do.")
	
def hint1():
	print( "1.Search around.")
	print( "2.Open the door")
	
def origi_room_map():
	print( """
	|====================================================================================================|
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|----------------| |-----------------------------|  |----------------------------|  |----------------|
	|                 1                                2                               3                 |
	|                                                 YOU                                                |
	|																									 |
	|===============================================||   ||==============================================|
	
	""")
	origi_room_hint()
	
def origi_room():
	origi_room_hint1()
	next = input("> ")
	if next == "1":
		door1_room_map()
		door1_room_action1()
	elif next == "2":
		door2_room_map()
		door2_room_action()
	elif next == "3":
		door3_room();
	else:
		unknow_input()
		origi_room()
		
def origi_room_hint():
	print( "Now you are in the castle.")
	print( "There are three doors in front of you.")
	
def origi_room_hint1():
	print( "1.Open the door1.")
	print( "2.Open the door2.")
	print( "3.Open the door3.")
	
def go_into_room():
	return 0
	
def door1_room_map():
	print( """
	|====================================================================================================|
	|                            |																		 |
	|                            |																		 |
	|                          	 |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|                          ^ |                                                                       |
	|                YOU      |_|                                                                        |
	|----------------| |-----------------------------|  |----------------------------|  |----------------|
	|                 1                                2                               3                 |
	|                                                                                                    |
	|																									 |
	|===============================================||   ||==============================================|
	
	""")
	print( "You come into the room.")
	print( "There is  a candle on your right.")
 
def door1_room_hint2():
	print( "You move along the wall.Find a deep hole in front of you.")
	print( "There is a pool on your left.")
	print( "You use the candle to find that a tigher is sitting on the other side.")
 
def door1_room_action1():
	print( "1.Take the candle")
	print( "2.Walk and search around.")
	next = input("> ")
	if next == "1":
		door1_room_hint2()
		door1_room_action2()
	elif next == "2":
		print( "You come across a tiger, and it eat you soon.")
		print( "Mission fails.")
	else:
		unknow_input()
		door1_room_action1()
	
def door1_room_action2():
	print( "1.Run away now.")
	print( "2.Jump into the pool.")
	print( "3.Scream out.")
	next = input("> ")
	if next == "1":
		print( "Unfortunately, tiger runs faster than you.")
		print( "You lose your legs and the head.")
		print( "Mission fails.")
	elif next == "2":
		print( "It is a nice choose. You swim to the other side and find a door there.")
		door1_room_map2()
		door1_room_out()
	elif next3 == "3":
		print( "Because of your screaming, the great devil comes and kills you immediately.")
	else:
		unknow_input()
		door1_room_action2()	
		
def door1_room_map2():
	print( """
	|====================================================================================================|
	|                            |																		 |
	|                            |																		 |
	|                _______   	 -                                                                       |
	|                |	p  | YOU -                                    	                                 |
	|                |  o  |     |                                                                       |
	|                |  o  |     |                                                                       |
	|                |  l  |     |                                                                       |
	|                |     |     |                                                                       |
	|      _______   |_____|     |                                                                       |
	|     | Tiger |              |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|----------------| |-----------------------------|  |----------------------------|  |----------------|
	|                 1                                2                               3                 |
	|                                                                                                    |
	|																									 |
	|===============================================||   ||==============================================|
		"""	)
 
def door1_room_out():
	hint1()
	next = input("> ")
	if next == "1":
		print( "Tiger catches you and you die." )
		print( "Mission fails.")
	elif next == "2":
		door2_room_map()
		door2_room_action()
	else:
		unknow_input()
		door1_room_out()
 
def door2_room_map():
	print( """
	|====================================================================================================|
	|                            |																		 |
	|                            |														|			|	 |
	|                _______   	 -  YOU                                                 |           |    |
	|                |	p  |     -                                    the great devil   |           |    |
	|                |  o  |     |                                                      |           |    |
	|                |  o  |     |                                                      |           |    |
	|                |  l  |     |                                                      |           |    |
	|                |     |     |                                                                       |
	|      _______   |_____|     |                                                                       |
	|     | Tiger |              |                                                                       |
	|                            |  |                                                                    |
	|                            |  |knife                                                               |
	|----------------| |-----------------------------|  |----------------------------|  |----------------|
	|                 1                                2                               3                 |
	|                                                                                                    |
	|																									 |
	|===============================================||   ||==============================================|
		"""	)
	print( "You look around, finding that the great devil is staring at you.")
	print( "You also find a knife that is on the corner on your right.")
 
def door2_room_action():
	print( "1.Run to the door2.")
	print( "2.Run to get the knife.")
	print( "3.Fight to the great devil.")
	next = input("> ")
	if next == "1":
		print( "Fail to run away, the great devil catch you and kill you.")
		print( "Mission fails.")
	elif next == "2":
		print( "Good job!Now you can fight against the great devil!")
		door2_room_action2()
	elif next == "3":
		print( "Because of strength disparity, you are killed by the great devil.")
		print( "Mission fails.")
	else:
		unknow_input()
		door2_room_action()
	
def door2_room_action2():
	print( "1.Fight against.")
	print( "2.Negociat with the great devil.")
	next = input("> ")
	if next == "1":
		fight_1()
	elif next == "2":
		print( "The great kill you finally.")
		print( "Mission fails.")
	else:
		unknow_input()
		door2_room_action2()
			
def fight_1():
	print( "You lose your leg.")
	print( "Do you want to continue?")
	print( "1.Fight against!")
	print( "2.Surrender to the great devil.")
	next = input("> ")
	if next == "1":
		print( "You are a hero. The God blesses you and help you defeat the great devil.")
		print( "Now you can take your princess away.")
		print( """
	|====================================================================================================|
	|                            |																		 |
	|                            |														|			|	 |
	|                _______   	 -                                                      |           |    |
	|                |	p  |     -                                                      |           |    |
	|                |  o  |     |                                                      |           |    |
	|                |  o  |     |                                                      |           |    |
	|                |  l  |     |                                                      |           |    |
	|                |     |     |                                                                       |
	|      _______   |_____|     |                                                                       |
	|     | Tiger |              |                                                                       |
	|                            |                                                                       |
	|                            |                                                                       |
	|----------------| |-----------------------------|  |----------------------------|  |----------------|
	|                 1                                2                               3                 |
	|                                                                                                    |
	|																									 |
	|===============================================||   ||==============================================|
											
										||||||||      |||||||
									   |		|	 |		 |
									  |		 ||||			  |
									 |  You and your princess  |
									  |						  |
									    |					|
										  |   			  |
											|		    |
											  |       |
												|   |
												  |
		"""	)	
	elif next == "2":
		print( "The great kill you finally.")
		print( "Mission fails.")
	else:
		unknow_input()
		fight_1()
		
def door3_room():
		print( "The great devil is looking at you. Bad luck, you dead.")
		exit(0)
		
def guard_room():
	return 0
	
def dini_room():
	return 0
	
def dog_room():
	return 0
	
def final_room():
	return 0
	
def hint():
	print( "I can not understand what you want to.")
 
def story_begin():
	print( "One day, when Qianqian was giving a concert in Shanghai, the devil appeared and took him away.")
	print( "Qianqian falled in danger.")
	print( "Many people wanted to save Qianqian,however,no one had succeeded ever.")
	print( "Many years later, you showed up and decided to rescue Qianqian.")
	print( "Then you comes to a gruesome castle.")
	print( """
	|====================================================================================================|
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|                                                                                                    |
	|===============================================||   ||==============================================|
	
	                                              YOU ARE HERE
	""" )
	
def game_process():
	hint1()
	next = input("> ")
	if next == "1":
		print( "Oh,shit!You falled into a deep hole!")
		print( """
		|====================================================================================================|
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|                                                                                                    |
		|===============================================||   ||==============================================|
									+++++
									+YOU+
									+++++
				""")
		search_around1()
	elif next == "2":
		origi_room_map()
		origi_room()
	else:
		unknow_input()
		game_process()
		
story_begin()
game_process()
