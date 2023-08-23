import sqlite3

def create_db():
    with sqlite3.connect('roster.db')as connection:
        conn = sqlite3.connect(':memory:')#this creates the database in RAM
        c = connection.cursor()
        c.executescript("""DROP TABLE IF EXISTS Roster;
                        CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)""")
        #created out table
        rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
        c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", rosterValues)
        #added data to the table
        c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
                  ('Human', 'Korben Dallas','100'))
        #updated one row of the table
        c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
        for row in c.fetchall():
            print(row)
        #pulled all rows where species was human


    
if __name__ == '__main__':
    create_db()
