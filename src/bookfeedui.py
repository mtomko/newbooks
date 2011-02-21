#!/usr/bin/env python
'''
Created on Feb 18, 2011

@author: Mark Tomko <mjt0229@gmail.com>
'''

from bookfeed import BookFeed
from view import BookFeedView
import Tkconstants
import Tkinter
import os
import tkFileDialog
import tkMessageBox

class TkBookFeedProcessor(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        Tkinter.Label(self, text='Select book feed:').pack()
        Tkinter.Button(self, text='Choose File', command=self.askopenfilename).pack(**button_opt)
        
        Tkinter.Label(self, text='Select output directory:').pack()
        Tkinter.Button(self, text='Choose Output Directory', command=self.askdirectory).pack(**button_opt)
        
        Tkinter.Button(self, text='Process', command=self.process).pack(**button_opt)

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

    def askopenfilename(self):
        '''
        Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        '''
        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
            self.__csvfile = filename;

    def askdirectory(self):
        """Returns a selected directoryname."""
        self.__output_directory = tkFileDialog.askdirectory(**self.dir_opt)
    
    def process(self):
        bookfeed = BookFeed(self.__csvfile)
        bookfeed.read()
    
        for fund in bookfeed.get_book_funds():
            output = open(os.path.join(self.__output_directory, fund + '.inc'), 'w')
            for book in bookfeed.get_books_by_fund(fund):
                output.write(BookFeedView(book).render())
            output.close()
        tkMessageBox.showinfo(message='Finished')

if __name__=='__main__':
    root = Tkinter.Tk()
    TkBookFeedProcessor(root).pack()
    root.mainloop()
