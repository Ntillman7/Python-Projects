import sqlite3


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    



conn=sqlite3.connect('file_db')
#creating database file



with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING \
        )")
        #creating a table within the database
    for file in fileList: #file is arbitrary name assigned for each item in the list fileList
        if file.endswith('.txt'): #pulling all items that end in .txt
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)",(file,))#using SQL to insert all values ending in txt into the database
            print(file)
    conn.commit()
conn.close()



