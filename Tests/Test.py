import unittest
import sqlite3
import os
import sys
os.chdir("..")
sys.path.insert(1, '{}/Resources'.format(os.getcwd))

def testDataBase():
    return

def testEntryObject():
    return

def testPasswordGeneration():
    return

def testEncryption():
    return

testDataBase()
testEntryObject()
testPasswordGeneration()
testEncryption()


# CreateEntry()
# CreateDataBase()

# if CheckState():
#     display("Password database found", 0)
#     display("Please enter key to decrypt the password database: ", 0)
#     DecryptKey = getpass.getpass()
#     DecryptDataBase(DecryptKey)

#     display("Select the number of the operation you would like to perform:", 0)
#     display("1 \tCreate a password?",0)
#     display("2 \tRetrieve a password?",0)
#     display("3 \tChange a password?",0)
#     display("4 \tRemove a password?",1)
#     choice = input()
#     display(choice,1)
# else:
#     newDB = input("would you like to create a new Password Database? (Y/N) ")
#     if(CheckAnswer(newDB)):
#         CreateDataBase()
#     else:
#         print("Goodbye!")
#         sys.exit()
# createDatabase()
# print(retrieveEntry("checksum"))
# addEntry("abc","123")
# b= retrieveEntry("abc")
# for i in b:
#     print(i)


# testing SQL DB calls
# def printall():
#     Cursor.execute("SELECT purpose FROM Passwords")
#     print(Cursor.fetchall())
# Connection = sqlite3.connect('UVault.db') 
# Cursor = Connection.cursor()
# dbfs.createDatabase()
# printall()
# entry = Entry("abc", 123)
# addEntry(entry)
# dbfs.addEntry(Entry("1234","12345123"))
# dbfs.addEntry(Entry("abd","afe"))
# dbfs.addEntry(Entry("234234","sferg"))
# printall()
# entry.password = "1235565"
# changeEntry(entry)
# printall()
# removeEntry(entry)
# printall()

# Connection.commit()
# Connection.close()
