# Anagrams Generated from here for 'poultry outwits ants' # http://ingesanagram.appspot.com/
import hashlib
phrase = 'poultry outwits ants'

words = open('abc.txt', 'r')
word_list = words.read().split('\n')

goal = 'e4820b45d2277f3844eac66c903e84be'

for word in word_list:
	hash_word = hashlib.md5(word).hexdigest()
	if hash_word == goal:
		print(word)
		break