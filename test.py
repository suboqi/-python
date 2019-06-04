# -*- coding:utf-8 -*
(venv) D:\python\笨办法学python>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait"
>>> words = ex25.brek_words(sentence)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'ex25' has no attribute 'brek_words'
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait
>>> wrods
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wrods' is not defined
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_last_word(sortes_words)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sortes_words' is not defined
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait
>>> ex25.print_first_and_last_sorted(sentence)
All
who
