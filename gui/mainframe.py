#!/usr/bin/env python

import Tkinter

class Mainframe:
    def __init__(self):
        root = Tkinter.Tk()
        root.title("pyTunes Media Player")       
        frame = Tkinter.Frame(root, width=500, height=300)
        frame.pack()
        root.mainloop()

