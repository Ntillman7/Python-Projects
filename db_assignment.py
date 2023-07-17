import sqlite3

conn=sqlite3.connect('file_db')
#creating database file

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING \
        )")
        #creating a table within the database
    conn.commit()
conn.close()



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
