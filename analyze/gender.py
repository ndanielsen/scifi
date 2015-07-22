#!/usr/bin/python -tt
"""
Counter words and gendered words
"""
from wordlists.gender_words import MALE_WORDS, FEMALE_WORDS




def word_counter(text): #opens the file and reads file. 

    word_dict = {}
    
    #return text
    words = text.translate(None, punc)
    words = words.lower().split() #splits the text into separate words
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1    
    for key in sorted(word_dict, key = word_dict.get, reverse = False):
            print "%s: %s" % (key, word_dict[key])   


def gender(text, gender_words_set):
	"""
	What do we do here?
	"""

	pass


def both_genders(text):
	"""
	returns a count of both male and female words in a tuple
	"""
	# hint call gendered in here twice

	pass




if __name__ == '__main__':
	print MALE_WORDS, FEMALE_WORDS