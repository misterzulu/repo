#!/usr/bin/env python

import Tkinter

class Mainframe:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.frame = Tkinter.Frame(self.root, width=200, height=100)
        self.frame.pack()
        self.root.mainloop()

