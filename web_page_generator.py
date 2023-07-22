import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.lbl_customText = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.lbl_customText.grid(row=0,column=0, padx=(30,30),pady=(10,10),sticky=N+W)

        self.txt_customText = tk.Entry(self.master, text='')
        self.txt_customText.grid(row=1,column=0, rowspan=1, columnspan=8, padx=(30,30),pady=(0,0),sticky=N+E+W)

        self.btn = Button(self.master, text="Default HTML Page", width = 30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=3, padx=(10,10), pady=(10,10), sticky=E)

        self.btn = Button(self.master, text="Submit Custom Text", width = 30, height=2, command=self.submitText)
        self.btn.grid(row=3, column=4, padx=(10,30), pady=(10,10), sticky=E)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent="<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def submitText(self):
        htmlCustomText= self.txt_customText.get()
        htmlFile = open("index.html", "w")
        htmlContent="<html>\n<body>\n<h1>" + htmlCustomText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        

if __name__ == "__main__":
    root=tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
