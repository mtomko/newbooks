#!/usr/bin/env python
'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''
from bookfeed import BookFeed
from view import BookFeedView

import datetime
import os
import sys
import Tkinter
import tkFileDialog
import tkMessageBox

class FileNamingScheme():
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    def __init__(self, extension='.php'):
        self.__month = FileNamingScheme.MONTHS[datetime.date.today().month - 1]
        self.__extension = extension
    
    def name_for(self, group):
        return BookFeed.normalize_group_name(group) + '-' + self.__month + self.__extension

class TkBookFeedProcessor(Tkinter.Frame):
    '''
    This class presents a simple GUI front-end to the Book Feed Processor
    '''
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
        
        # set up UI instance variables
        self.__mapfile = Tkinter.StringVar()
        self.__feedfile = Tkinter.StringVar()
        self.__output_directory = Tkinter.StringVar()

        # define interface elements
        # select fund/group map
        Tkinter.Label(self, text='Group map:').grid(row=0, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_map_file).grid(row=0, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.mapfile_entry = Tkinter.Entry(self, textvariable=self.__mapfile, state="readonly", width=64)
        self.mapfile_entry.grid(row=0, column=2, sticky=Tkinter.E)
        
        # select input file
        Tkinter.Label(self, text='Book feed:').grid(row=1, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_feed_file).grid(row=1, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.feedfile_entry = Tkinter.Entry(self, textvariable=self.__feedfile, state="readonly", width=64)
        self.feedfile_entry.grid(row=1, column=2, sticky=Tkinter.E)

        # select output directory
        Tkinter.Label(self, text='Output directory:').grid(row=2, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.__prompt_output_dir).grid(row=2, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.output_dir_entry = Tkinter.Entry(self, textvariable=self.__output_directory, state="readonly", width=64)
        self.output_dir_entry.grid(row=2, column=2, sticky=Tkinter.E)
        
        # execute process
        Tkinter.Button(self, text='Process', command=self.__process).grid(row=3, column=0, sticky=Tkinter.W, padx=5, pady=5)
        Tkinter.Button(self, text='Quit', command=self.__quit).grid(row=3, column=1, columnspan=2, sticky=Tkinter.W, padx=5, pady=5)

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
        

    def __prompt_map_file(self):
        '''Prompts the user to select a fund code mapping file and saves the filename'''
        self.__mapfile.set(tkFileDialog.askopenfilename(**self.file_opt))
            
    def __prompt_feed_file(self):
        '''Prompts the user to select a feed file and saves the filename'''
        self.__feedfile.set(tkFileDialog.askopenfilename(**self.file_opt))

    def __prompt_output_dir(self):
        '''Prompts the user to select an output directory and saves the location'''
        output_dir = tkFileDialog.askdirectory(**self.dir_opt)

        if output_dir:
            self.__output_directory.set(output_dir)
    
    @staticmethod
    def __process_file(mapfile, feedfile, output_dir):
        name_scheme = FileNamingScheme()
        bookfeed = BookFeed(feedfile, mapfile)
        bookfeed.read()
    
        for group in bookfeed.get_book_groups():
            output = open(os.path.join(output_dir, name_scheme.name_for(group)), 'w')
            for book in bookfeed.get_books_by_group(group):
                output.write(BookFeedView(book).render())
            output.close()
                
    def __process(self):
        mapfile = self.__mapfile.get()
        feedfile = self.__feedfile.get()
        output_dir = self.__output_directory.get()
        if not mapfile:
            tkMessageBox.showerror(title='Process', message='Please select a group map')
        elif not feedfile:
            tkMessageBox.showerror(title='Process', message='Please select a book feed')
        elif not output_dir:
            tkMessageBox.showerror(title='Process', message='Please select an output directory')
        else:
            try:
                TkBookFeedProcessor.__process_file(mapfile, feedfile, output_dir)
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
