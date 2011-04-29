'''
Created on Apr 29, 2011

@author: mark
'''
import csv

class GroupMap(object):
    '''
    'Abstract' base class for mapping functions.
    '''
    def group_for(self, book):
        pass

class CompositeGroupMap(GroupMap):
    def __init__(self, maps, default=None):
        self.__default = default
        self.__maps = maps
    
    def group_for(self, book):
        '''
        Attempts to use each map in succession; uses the value from the first
        map that provides an actual value
        '''
        for map in self.__maps:
            group = map.group_for(book)
            if group != None:
                return group
        return self.__default

class CallNumberPrefixMap(GroupMap):
    '''
    Represents a mapping from fund codes to book groups
    '''
    def __init__(self, file, default):
        self.__default = default
        self.__map = CallNumberPrefixMap.read(file)
    
    @staticmethod
    def read(csvfile):
        mapfile = csv.reader(open(csvfile, 'rU'), delimiter=',', quotechar='"')
        map = {}
        rownum = 0
        for row in mapfile:
            if rownum > 0:
                call_no_pfx = row[0].strip().upper()
                group = row[1].strip()
                map[call_no_pfx] = group
            rownum += 1
        return map
    
    def group_for(self, book):
        if book.call_no()[0] in self.__map.keys():
            return self.__map[book.call_no()[0]]
        return self.__default

class FundGroupMap(GroupMap):
    '''
    Represents a mapping from fund codes to book groups
    '''
    def __init__(self, file, default):
        self.__default = default
        self.__map = FundGroupMap.read(file)
    
    @staticmethod
    def read(csvfile):
        mapfile = csv.reader(open(csvfile, 'rU'), delimiter=',', quotechar='"')
        map = {}
        rownum = 0
        for row in mapfile:
            if rownum > 0:
                fund = row[0].strip()
                group = row[1].strip()
                map[fund] = group
            rownum += 1
        return map
    
    def group_for(self, book):
        if book.fund_code() in self.__map.keys():
            return self.__map[book.fund_code()]
        return self.__default
