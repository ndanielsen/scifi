#!/usr/bin/python -tt
# homework2_functions.py - solving the problems for homework2
import os
import requests

CONSTANT = 1


def open_file(file_input): #downloads the book from Project Guttenburg and writes to a file
    
    NCONSTANT = 2

    url, text_name = file_input

    text_name = 'data/' + text_name

    if os.path.isfile(text_name):
        print "%s file already here" % text_name
        
    else:
        # print url, text_name
        text_file = requests.get(url, verify = False)
        text_file = text_file.content
        file_ref = open(text_name,"w+")
        file_ref.write(text_file)
        print '%s file downloaded' % text_name
    
    return text_name     

def open_several_files(file_inputs):

    for afile in file_inputs:
        open_file(afile)

    return [text_name for url, text_name in file_inputs]
    

if __name__ == '__main__':
	files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]

	assert open_several_files(files) == ['frank_text.txt', 'dr_JEKYLL.txt']

	print NCONSTANT
