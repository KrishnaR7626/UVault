# Database Functions
import sqlite3
from Entry import Entry

def createDatabase(Cursor):
    Cursor.execute("CREATE TABLE Passwords(purpose text, password text)")
    entry = Entry("checksum", "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")
    addEntry(Cursor, entry)

def addEntry(Cursor, entry):
    Cursor.execute("INSERT INTO Passwords VALUES(?, ?)", (entry.purpose, entry.password))

def removeEntry(Cursor, purpose):
    Cursor.execute("DELETE FROM Passwords WHERE purpose = ?", (purpose,))
    
def changeEntry(Cursor, entry):
    Cursor.execute("UPDATE Passwords SET password = ? WHERE purpose = ?",(entry.password, entry.purpose))

def retrieveEntry(Cursor, purpose):
    Cursor.execute("SELECT password FROM Passwords WHERE purpose = ?", (purpose,))
    password = Cursor.fetchone()
    if password != None:
        return password[0]
    else:
        return password