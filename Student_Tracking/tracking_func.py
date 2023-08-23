
#Python Ver:    3.11.3
#
#Author:        Nichol Tillman
#
#Purpose:       Phonebook Demo. Using OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
#Tested OS:     This code was written and tested in Windows 10.


import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox


import tracking_main
import tracking_gui


def create_db(self):
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        #cursor is required to use syntax
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def submit(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip() 
    var_lname = var_lname.strip() 
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_email.get().strip()

    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_phone,col_email,col_course) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_phone,var_email,var_course))
        self.lstList1.insert(END, var_fname)
        conn.commit()
    conn.close()
    

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) 
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM tbl_students WHERE col_fname= '{}'""".format(var_select))
        conn.commit()
    conn.close()




if __name__ == "__main__":
    pass
