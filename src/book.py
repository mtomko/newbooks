'''
Created on Apr 29, 2011

@author: mark
'''

class Book(object):
    '''
    Represents a new book; we store only the OCLC number and the catalog
    number from Millennium.
    '''
    def __init__(self, oclc, record, call_no, fund_code):
        self.__oclc = oclc
        self.__record = record
        self.__call_no = call_no
        self.__fund_code = fund_code
    
    def oclc_number(self):
        return self.__oclc

    def record_number(self):
        return self.__record
    
    def call_no(self):
        return self.__call_no
    
    def fund_code(self):
        return self.__fund_code
