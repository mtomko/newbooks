'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''

import csv

class Book(object):
    '''
    Represents a new book; we store only the OCLC number and the catalog
    number from Millennium.
    '''
    def __init__(self, oclc, record):
        self.__oclc = oclc
        self.__record = record
    
    def oclc_number(self):
        return self.__oclc

    def record_number(self):
        return self.__record

class BookFeed(object):
    '''
    Processes a simple report containing data about books; assumes CSV format
    and expects a header in the first row; uses that header to figure out what
    the column order is, but the headers should have the following information:
    
    "RECORD #(BIBLIO)","OCLC #","FUND"
    '''
    RECORD_KEY = 'RECORD #(BIBLIO)'
    OCLC_KEY = 'OCLC #'
    FUND_KEY = 'FUND'

    def __init__(self, file):
        self.__csvfile = file
        self.__books = {}
    
    def read(self):
        feed = csv.reader(open(self.__csvfile, 'rb'), delimiter=',', quotechar='"')
        key = {}
        rownum = 0
        for row in feed:
            if rownum == 0:
                # it's a header, so let's figure out what's what
                colnum = 0
                for col in row:
                    key[col] = colnum
                    colnum += 1
            else:
                # it's a data row, so let's get the book!
                fund = row[key[BookFeed.FUND_KEY]].strip()
                if fund == '':
                    fund = 'general'
                record = row[key[BookFeed.RECORD_KEY]]
                oclc = row[key[BookFeed.OCLC_KEY]]
                if self.__books.has_key(fund):
                    self.__books[fund].append(Book(oclc, record))
                else:
                    self.__books[fund] = [Book(oclc, record)]
            rownum += 1
    
    def get_book_funds(self):
        return self.__books.keys()
    
    def get_books_by_fund(self, fund):
        if self.__books.has_key(fund):
            return self.__books[fund]
        return []