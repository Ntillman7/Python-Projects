#Python Ver:    3.11.3
#
#Author:        Nichol Tillman
#
#Purpose:       Phonebook Demo. Using OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
#Tested OS:     This code was written and tested in Windows 10.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

#importing other modules
import phonebook_gui
import phonebook_func

#Frame is the parent class from tkinter
class ParentWindow(Frame):
    def __inti__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defines master frame configuration
        self.master = master
        self.master.minsize(500,300) #height and width
        self.master.maxsize(500,300)
        #CenterWindow method is used to center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.config(bg="#F0F0F0")
        #this protocol method is built into tkinter to catch if the user cliccks the 'X' on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master
    

        #load in the GUI widgets from a seperate module, keeping code compartmentalized and uncluttered
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')

        
"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""


if __name__ == "__main__":
    root = tk.Tk()
    #sytax to create window from tkinter
    App = ParentWindow(root)
    #sytax passses the window to our class
    root.mainloop()
    #loops so that window does not dissapear
