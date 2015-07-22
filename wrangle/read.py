#!/usr/bin/python -tt
"""
Reads file into memory
"""



def read_file(filename):
    
	with open(filename, 'r+') as file_ref:
		
		text = file_ref.read()
	return text 

def remove_html(text):

	pass




if __name__ == '__main__':

	read_file('data/frank_text.txt')