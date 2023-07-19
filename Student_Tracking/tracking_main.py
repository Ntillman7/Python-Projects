#Python Ver:    3.11.3
#
#Author:        Nichol Tillman
#
#Purpose:       Student Tracking Assignment. Using OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
#Tested OS:     This code was written and tested in Windows 10.



from tkinter import *
import tkinter as tk

import tracking_gui
import tracking_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

    
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(900, 500))
        self.master.title('Student Tracking')
        self.master.config(bg='lightgray')
        arg = self.master

        tracking_gui.load_gui(self)

        



if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop() #causes it to conitually run and stay open
