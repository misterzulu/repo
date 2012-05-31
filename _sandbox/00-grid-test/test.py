#!/usr/bin/env python

import Tkinter
from Tkinter import *
#from Tkinter import ttk
p=Tkinter.Tk()
t=ttk.Treeview(p)
t["columns"]=("first","second")
t.column("first",width=75,anchor="center" )
t.column("second",width=100)
t.heading("first",text="first column")
t.heading("second",text="second column")
t.insert("",0,"dir1",text="directory 1")
t.insert("dir1","end","dir 1",text="file 1 1",values=("file 1 A","file 1 B"))
id=t.insert("","end","dir2",text="directory 2")
t.insert("dir2","end",text="dir 2",values=("file 2 A","file 2 B"))
t.insert(id,"end",text="dir 3",values=("val 1 ","val 2"))
t.insert("",0,text="first line",values=("first line 1","first line 2"))
t.tag_configure("ttk")
t.pack(side=BOTTOM,fill=X)
p.mainloop()
