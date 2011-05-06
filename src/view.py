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

class Navigation(pystache.View):
    def __init__(self, name_scheme, group, page_number, total_pages):
        super(Navigation, self).__init__(template=None, context={})
        self.__name_scheme = name_scheme
        self.__group = group
        self.__page_number = page_number
        self.__total_pages = total_pages
    
    def nextlink(self):
        return self.__page_number < self.__total_pages
    
    def next(self):
        return self.__name_scheme.name_for(self.__group, self.__page_number + 1)
    
    def previouslink(self):
        return self.__page_number > 1
    
    def previous(self):
        return self.__name_scheme.name_for(self.__group, self.__page_number - 1)
    
        
        