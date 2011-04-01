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

class FundGroupMap(object):
    '''
    Represents a mapping from fund codes to book groups
    '''
    def __init__(self, file):
        self.__map = FundGroupMap.read(file)
    
    @staticmethod
    def read(csvfile):
        mapfile = csv.reader(open(csvfile, 'rb'), delimiter=',', quotechar='"')
        map = {}
        rownum = 0
        for row in mapfile:
            if rownum > 0:
                fund = row[0].strip()
                group = row[1].strip()
                map[fund] = group
            rownum += 1
        return map
    
    def group_for(self, fund, default='Other'):
        if fund in self.__map.keys():
            return self.__map[fund]
        return default

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
    
    DELETE_TABLE = string.maketrans(string.letters, ' ' * len(string.letters))

    def __init__(self, feedfile, mapfile):
        self.__map = FundGroupMap(mapfile)
        self.__feedfile = feedfile
        self.__books = {}
    
    def read(self):
        '''
        Reads the book feed file.
        '''
        # open the CSV file for reading in binary mode - this has no effect on
        # Mac/Unix, but may be important for Windows
        # see http://docs.python.org/tutorial/inputoutput.html#reading-and-writing-files
        feed = csv.reader(open(self.__feedfile, 'rb'), delimiter=',', quotechar='"')

        # assume that columns are in the default order
        key = BookFeed.__default_column_key()
        rownum = 0
        for row in feed:
            if rownum == 0:
                # figure out if we have a header describing the columns
                if row[0] in (BookFeed.RECORD_KEY, BookFeed.OCLC_KEY, BookFeed.FUND_KEY):
                    key = BookFeed.__build_column_key(row)
                else:                    
                    # we still need to process this book, since it wasn't a header
                    self.__read_book_row(row, key)
            else:
                # it's a data row, so let's get the book!
                self.__read_book_row(row, key)
            rownum += 1
    
    def get_book_groups(self):
        '''
        Returns the list of book groups found in the book feed
        '''
        return self.__books.keys()
    
    def get_books_by_group(self, group):
        '''
        Returns the list of books associated with the provided group
        '''
        if self.__books.has_key(group):
            return self.__books[group]
        return []
    
    @staticmethod
    def normalize_group_name(raw_group_name):
        return raw_group_name.translate(None, BookFeed.DELETE_TABLE)

    @staticmethod
    def __default_column_key():
        return { BookFeed.RECORD_KEY : 0, BookFeed.OCLC_KEY : 1, BookFeed.FUND_KEY : 2 }
    
    @staticmethod
    def __build_column_key(row):
        key = {}
        # it's a header, so let's figure out what's what
        colnum = 0
        for col in row:
            key[col] = colnum
            colnum += 1
        return key

    def __read_book_row(self, row, key):
        '''
        Reads a single row in the book feed and adds
        a book record to the self.__books list.
        '''
        fund = row[key[BookFeed.FUND_KEY]].strip()
        record = row[key[BookFeed.RECORD_KEY]][0:8]
        oclc = row[key[BookFeed.OCLC_KEY]]
        
        group = self.__map.group_for(fund)
        if self.__books.has_key(group):
            self.__books[group].append(Book(oclc, record))
        else:
            self.__books[group] = [Book(oclc, record)]
        
        