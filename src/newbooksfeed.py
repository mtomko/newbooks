#!/usr/bin/env python
'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''

from bookfeed import BookFeed
from view import BookFeedView

import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Provide a feed to process'

    report = sys.argv[1]
    bookfeed = BookFeed(report)
    bookfeed.read()
    
    for fund in bookfeed.get_book_funds():
        output = open(fund + '.inc', 'w')
        for book in bookfeed.get_books_by_fund(fund):
            output.write(BookFeedView(book).render())
        output.close()