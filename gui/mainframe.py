#!/usr/bin/env python

'''avoid conflicts between 2 Image classes of Tkinter & PIL '''
import Tkinter as tk
from PIL import Image, ImageTk

class Mainframe:

    def __init__(self):

        # Tkinter root window
        root = tk.Tk()
        root.title("pyTunes Media Player")       
        
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))

        # Header frame
        header_frame = tk.Frame(root, width=w, height=h)
        header_frame.pack()
        
        img_bg_header = ImageTk.PhotoImage(Image.open("bitmap/bg_header.png"))
        panel_header = tk.Label(header_frame, image=img_bg_header)
        panel_header.pack(side="top", fill="both", expand="yes")
        
        # Paned window
        # PanedWindow bg=black >> this gives the color to the sash
        paned_window = tk.PanedWindow(orient="horizontal", relief="ridge", bg="black")
        paned_window.pack(fill="both", expand=1)

        left_panel = tk.Label(paned_window, text="left panel")
        paned_window.add(left_panel)

        right_panel = tk.Label(paned_window, text="right panel")
        paned_window.add(right_panel)



#        content_frame = tk.Frame(root, width=w, height=h)
#        content_frame.configure(background="powder blue")
#        content_frame.pack()        
        
        root.mainloop()
