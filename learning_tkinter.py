import tkinter
#creates GUI
from tkinter import *
#imports all widgets for tkinter



class ParentWindow(Frame):#Frame is parent class from tkinter
    def __init__ (self, master):
    #frame = master, class = self
        Frame.__init__(self)
        #copy from here up for your code

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')
        #create basic window for tkinter

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname = Label(self.master, text= 'First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFname.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.lblLname = Label(self.master, text= 'Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLname.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        self.lblDisplay = Label(self.master, text= '', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        
        self.txtFname = Entry(self.master, text=self.varFname, font=("Helvetica", 16), fg='black', bg='lightblue')
        #entry is function from tkinter for basic one line text box
        self.txtFname.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))
        #pack instead of grid stacks the boxes on top of each other with nothing else in ()
        
        self.txtLname = Entry(self.master, text=self.varLname, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLname.grid(row=1,column=1, padx=(30, 0), pady=(30, 0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        #in Button() is blueprint of how we want it to look
        #command is what will happen when you click the button
        self.btnSubmit.grid(row=2,column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello, {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()
        #destroy closes the window 
        



#you also need this section in every code to make the window work
if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop() #causes it to conitually run and stay open
