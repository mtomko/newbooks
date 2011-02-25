'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''
import csv
import string

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
    GROUP_KEY = 'GROUP'
    
    DELETE_TABLE = string.maketrans(string.letters, ' ' * len(string.letters))

    def __init__(self, file):
        self.__csvfile = file
        self.__books = {}
    
    def read(self):
        feed = csv.reader(open(self.__csvfile, 'rb'), delimiter=',', quotechar='"')
        key = {}
        rownum = 0
        for row in feed:
            if rownum == 0:
                # figure out if we have a header
                if row[0] in (BookFeed.RECORD_KEY, BookFeed.OCLC_KEY, BookFeed.GROUP_KEY):
                    # it's a header, so let's figure out what's what
                    colnum = 0
                    for col in row:
                        key[col] = colnum
                        colnum += 1
                else:
                    # it's not a header, so we need to make some guesses
                    key[BookFeed.RECORD_KEY] = 0
                    key[BookFeed.OCLC_KEY] = 1
                    key[BookFeed.GROUP_KEY] = 2
                    
                    # we still need to process this book, since it wasn't a header
                    self.read_book_row(row, key)
            else:
                # it's a data row, so let's get the book!
                self.read_book_row(row, key)
            rownum += 1
    
    def read_book_row(self, row, key):
        group = row[key[BookFeed.GROUP_KEY]].strip()
        if group == '':
            group = 'Other'
        record = row[key[BookFeed.RECORD_KEY]]
        oclc = row[key[BookFeed.OCLC_KEY]]
        if self.__books.has_key(group):
            self.__books[group].append(Book(oclc, record))
        else:
            self.__books[group] = [Book(oclc, record)]
    
    def get_book_groups(self):
        return self.__books.keys()
    
    def get_books_by_fund(self, group):
        if self.__books.has_key(group):
            return self.__books[group]
        return []
    
    @staticmethod
    def normalize_group_name(raw_group_name):
        return raw_group_name.translate(None, BookFeed.DELETE_TABLE)
        
        