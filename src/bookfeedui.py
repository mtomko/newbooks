#!/usr/bin/env python
'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''
from bookfeed import BookFeed
from view import BookFeedView
import Tkinter
import os
import sys
import tkFileDialog
import tkMessageBox

class TkBookFeedProcessor(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
        
        # set up UI instance variables
        self.__csvfile = Tkinter.StringVar()
        self.__output_directory = Tkinter.StringVar()

        # define interface elements
        # select input file
        Tkinter.Label(self, text='Select book feed:').grid(row=0, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.prompt_feed_file).grid(row=0, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.file_entry = Tkinter.Entry(self, textvariable=self.__csvfile, state="readonly", width=64)
        self.file_entry.grid(row=0, column=2, sticky=Tkinter.E)

        # select output directory
        Tkinter.Label(self, text='Select output directory:').grid(row=1, column=0, sticky=Tkinter.W)
        Tkinter.Button(self, text='Choose', command=self.prompt_output_dir).grid(row=1, column=1, sticky=Tkinter.W, padx=5, pady=5)
        self.output_dir_entry = Tkinter.Entry(self, textvariable=self.__output_directory, state="readonly", width=64)
        self.output_dir_entry.grid(row=1, column=2, sticky=Tkinter.E)
        
        # execute process
        Tkinter.Button(self, text='Process', command=self.process).grid(row=2, column=0, sticky=Tkinter.W, padx=5, pady=5)
        Tkinter.Button(self, text='Quit', command=self.quit).grid(row=2, column=1, columnspan=2, sticky=Tkinter.W, padx=5, pady=5)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['parent'] = root
        options['title'] = 'Choose book feed file'

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Choose an output directory'

    def prompt_feed_file(self):
        '''
        This time the dialog just returns a filename and the file is opened by your own code.
        '''
        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
            self.__csvfile.set(filename)

    def prompt_output_dir(self):
        """Returns a selected directoryname."""
        output_dir = tkFileDialog.askdirectory(**self.dir_opt)

        if output_dir:
            self.__output_directory.set(output_dir)
    
    @staticmethod
    def process_file(file, output_dir):
        bookfeed = BookFeed(file)
        bookfeed.read()
    
        for group in bookfeed.get_book_groups():
            output = open(os.path.join(output_dir, BookFeed.normalize_group_name(group) + '.inc'), 'w')
            for book in bookfeed.get_books_by_fund(group):
                output.write(BookFeedView(book).render())
            output.close()
                
    def process(self):
        self.process_file(self.__csvfile.get(), self.__output_directory.get())
        tkMessageBox.showinfo(message='Finished')
        
    def quit(self):
        self.destroy()
        sys.exit()

if __name__=='__main__':
    root = Tkinter.Tk()
    TkBookFeedProcessor(root).pack()
    root.mainloop()
