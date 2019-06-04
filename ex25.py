# -*- coding:utf-8 -*-
#
def break_words(stuff):
#这个函数将会为我们分解单词
	"""This function will break up words for us."""
	words = stuff.split(" ")
	return words
#
def sort_words(words):
	#整理单词
	"""Sorts the words."""
	return sorted(words)
#
def print_first_word(words):
	#在弹出后打印第一个单词
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print(word)
#
def print_last_word(words):
	#打印弹出后的最后一个字
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print(word)
#
def sort_sentence(sentence):
	#接受一个完整的句子并返回已排序的单词
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
#
def print_first_and_last(sentence):
	#打印句子的第一个和最后一个单词
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
#
def print_first_and_last_sorted(sentence):
    #然后打印第一个和最后一个单词
	"""sotrs the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
