'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''
import pystache

class BookFeedView(pystache.View):
    '''
    Represents a Mustache view of a new book. For information about mustache, 
    see:
    http://mustache.github.com/
    https://github.com/defunkt/pystache/
    '''
    def __init__(self, book):
        super(BookFeedView, self).__init__(template=None, context={})
        self.__book = book

    def oclc(self):
        return self.__book.oclc_number()
    
    def record(self):
        return self.__book.record_number()