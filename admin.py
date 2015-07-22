#!/usr/bin/python -tt

from scraper.ingest import open_several_files





if __name__ == '__main__':
	

	files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]

	assert open_several_files(files) == ['frank_text.txt', 'dr_JEKYLL.txt']


	pass

