#!/usr/bin/env python
'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''
from bookfeed import BookFeed
from view import BookFeedView, Navigation

import datetime
import os
import sys
import Tkinter
import tkFileDialog
import tkMessageBox

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class NamingScheme():
    def name_for(self, group, number):
        pass

class FileNamingScheme(NamingScheme):
    def __init__(self, month, extension='.php'):
        self.__month = month
        self.__extension = extension
    
    def set_month(self, month):
        self.__month = month
    
    def name_for(self, group, number=1):
        return BookFeed.normalize_group_name(group) + '-' + self.__month + '-' + str(number) + self.__extension

class PageNamingScheme(NamingScheme):
    def __init__(self, month, page='newbooks.php'):
        self.__month = month
        self.__page = page
    
    def set_month(self, month):
        self.__month = month
    
    def name_for(self, group, number=1):
        return self.__page + '?c=' + group + '&m=' + self.__month + '&p=' + str(number)


class BookFeedProcessor():
    MAX_BOOKS_PER_PAGE = 100
    
    def __init__(self):
        pass
    
    @staticmethod
    def process_feed(callnomapfile, fundmapfile, feedfile, month, output_dir):
        file_name_scheme = FileNamingScheme(month)
        page_name_scheme = PageNamingScheme(month)
        bookfeed = BookFeed(feedfile, callnomapfile, fundmapfile)
        bookfeed.read()
        
        for group in bookfeed.get_book_groups():
            output = open(os.path.join(output_dir, file_name_scheme.name_for(group)), 'w')
            
            books = bookfeed.get_books_by_group(group)
            
            page_number = 1
            total_pages = len(books) / BookFeedProcessor.MAX_BOOKS_PER_PAGE + 1
            
            book_number = 0
            for book in books:
                if book_number > BookFeedProcessor.MAX_BOOKS_PER_PAGE - 1:
                    # this is the last book for the page, so write the navigation
                    output.write(Navigation(page_name_scheme, group, page_number, total_pages).render())
                    output.close()
                    # move to the next page
                    page_number += 1
                    book_number = 0
                    output = open(os.path.join(output_dir, file_name_scheme.name_for(group, page_number)), 'w')

                book_number += 1
                output.write(BookFeedView(book).render())

            output.write(Navigation(page_name_scheme, group, page_number, total_pages).render())
            output.close()

class TkBookFeedProcessor(Tkinter.Frame):
    MAX_BOOKS_PER_PAGE = 100
    '''
    This class presents a simple GUI front-end to the Book Feed Processor
    '''
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
        
        # set up UI instance variables
        self.__callnomapfile = Tkinter.StringVar()
        self.__fundmapfile = Tkinter.StringVar()
        self.__feedfile = Tkinter.StringVar()
        self.__month = Tkinter.StringVar()
        self.__output_directory = Tkinter.StringVar()

        # define interface elements
        # select fund/group map
        Tkinter.Label(self, text='Fund Group map:').grid(row=0, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_fundmap_file).grid(row=0, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.fundmapfile_entry = Tkinter.Entry(self, textvariable=self.__fundmapfile, state="readonly", width=64)
        self.fundmapfile_entry.grid(row=0, column=2, sticky=Tkinter.E)

        # select call number group map
        Tkinter.Label(self, text='Call Number map:').grid(row=1, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_callnomap_file).grid(row=1, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.callnomapfile_entry = Tkinter.Entry(self, textvariable=self.__callnomapfile, state="readonly", width=64)
        self.callnomapfile_entry.grid(row=1, column=2, sticky=Tkinter.E)
        
        # select input file
        Tkinter.Label(self, text='Book feed:').grid(row=2, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_feed_file).grid(row=2, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.feedfile_entry = Tkinter.Entry(self, textvariable=self.__feedfile, state="readonly", width=64)
        self.feedfile_entry.grid(row=2, column=2, sticky=Tkinter.E)

        # select output directory
        Tkinter.Label(self, text='Output directory:').grid(row=3, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_output_dir).grid(row=3, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.output_dir_entry = Tkinter.Entry(self, textvariable=self.__output_directory, state="readonly", width=64)
        self.output_dir_entry.grid(row=3, column=2, sticky=Tkinter.E)
        
        # select month
        Tkinter.Label(self, text='Select Month:').grid(row=4, column=0, sticky=Tkinter.W)
        self.__month.set(MONTHS[datetime.date.today().month - 1])
        w = apply(Tkinter.OptionMenu, (self, self.__month) + tuple(MONTHS))
        w.grid(row=4, column=1, sticky=Tkinter.W)
        
        # execute process
        Tkinter.Button(self, text='Process', command=self.__process).grid(row=5, column=0, sticky=Tkinter.W, padx=5, pady=5)
        Tkinter.Button(self, text='Quit', command=self.__quit).grid(row=5, column=1, columnspan=2, sticky=Tkinter.W, padx=5, pady=5)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt'), ('comma-separated values', '.csv')]
        options['parent'] = root
        options['title'] = 'Choose book feed file'

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Choose an output directory'
        

    def __prompt_file(self, file):
        file.set(tkFileDialog.askopenfilename(**self.file_opt))

    def __prompt_callnomap_file(self):
        '''Prompts the user to select a fund code mapping file and saves the filename'''
        self.__prompt_file(self.__callnomapfile)

    def __prompt_fundmap_file(self):
        '''Prompts the user to select a fund code mapping file and saves the filename'''
        self.__prompt_file(self.__fundmapfile)
            
    def __prompt_feed_file(self):
        '''Prompts the user to select a feed file and saves the filename'''
        self.__prompt_file(self.__feedfile)

    def __prompt_output_dir(self):
        '''Prompts the user to select an output directory and saves the location'''
        output_dir = tkFileDialog.askdirectory(**self.dir_opt)

        if output_dir:
            self.__output_directory.set(output_dir)
                
    def __process(self):
        callnomapfile = self.__callnomapfile.get()
        fundmapfile = self.__fundmapfile.get()
        feedfile = self.__feedfile.get()
        month = self.__month.get()
        output_dir = self.__output_directory.get()
        if not callnomapfile:
            tkMessageBox.showerror(title='Process', message='Please select a call number map')
        elif not fundmapfile:
            tkMessageBox.showerror(title='Process', message='Please select a fund map')
        elif not feedfile:
            tkMessageBox.showerror(title='Process', message='Please select a book feed')
        elif not output_dir:
            tkMessageBox.showerror(title='Process', message='Please select an output directory')
        else:
            try:
                BookFeedProcessor.process_feed(callnomapfile, fundmapfile, feedfile, month, output_dir)
                tkMessageBox.showinfo(message='Finished')
            except Exception as e:
                print repr(e)
                tkMessageBox.showerror(title='Process', message=repr(e))

    def __quit(self):
        self.destroy()
        sys.exit()

if __name__=='__main__':
    root = Tkinter.Tk()
    root.title('Book Feed Processor')
    TkBookFeedProcessor(root).pack()
    root.mainloop()
