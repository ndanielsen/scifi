#!/usr/bin/python -tt

from scraper.ingest import open_several_files
from wrangle.read import read_file
from analyze.gender import word_counter, gender, both_genders


def main():

	summary = {}

	filenames = open_several_files(files)

	for filename in filenames:
		text = read_file(filename)
		count = word_counter(text)
		genderedwords = both_genders(text)

		# store the report in the dictionary for each hint: add keys and nested dictionsaries
	pass







if __name__ == '__main__':
	

	files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]

	assert open_several_files(files) == ['frank_text.txt', 'dr_JEKYLL.txt']

	print read_file('data/frank_text.txt')
	
	pass

