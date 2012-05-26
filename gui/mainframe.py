#!/usr/bin/env python

import Tkinter

class Mainframe:
    def __init__(self):
        root = Tkinter.Tk()
        root.title("pyTunes Media Player")       
        frame = Tkinter.Frame(root, width=200, height=100)
        frame.pack()
        root.mainloop()

