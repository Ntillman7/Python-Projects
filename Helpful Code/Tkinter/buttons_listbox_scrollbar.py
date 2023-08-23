# how to make a listbox with a scrollbar
from tkinter import *

win= Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill = Y)
#next 2 lines connect the listbox and the scrollbar
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
#next line allows you to create a tuple based on a selected item in the listbox
lb.curselection()
(2,)


#how to put buttons in a box using a frame and add functionality
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text = "Two")
b3 = Button(f, text = "Three")
b1.pack(side=LEFT)
b2.pack(side = LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()
b1.configure(text = "Uno")
def but1():
    print("Button one was pushed")


#how to put buttons in a box and orient them
    from tkinter import *
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text = "Two")
b1.pack()
b2.pack()
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b3 = Button(win, text = "Three")
b3.pack(side = RIGHT, padx = 10)
b4 = Button(win, text = "Four")
b4.pack( side = BOTTOM, pady = 10)
b4.pack( side = BOTTOM, pady = 10)
b4.pack( side = BOTTOM)
b5 = Button(win, text="Five")
b5.pack(side = BOTTOM)
