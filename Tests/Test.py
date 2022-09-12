import unittest
import sqlite3
import os
import sys
os.chdir("..")
path = os.getcwd()+'/Python'
sys.path.insert(1, path)
from Entry import Entry
import DatabaseFunctions as DatabaseFunctions
import PasswordGenerationFunctions as PasswordGenerationFunctions
import DatabaseEncryptionFunctions as DatabaseEncryptionFunctions
os.chdir("Tests")

# sys.path.insert(1, '{}/Resources'.format(os.getcwd))
# sys.path.insert(1, '{}/Resources'.format(os.getcwd))
# sys.path.insert(1, '{}/Resources'.format(os.getcwd))
# sys.path.insert(1, '{}/Resources'.format(os.getcwd))
# sys.path.insert(1, '{}/Resources'.format(os.getcwd))
Connection = sqlite3.connect('UVault.db') 
Cursor = Connection.cursor()
class UVaultTests(unittest.TestCase):
    def testDataBase(self):
        DatabaseFunctions.createDatabase(Cursor)
        entry1 = Entry("User1", "Password1")
        entry2 = Entry("User2", "Password2")
        entry3 = Entry("User3", "Password3")
        entry4 = Entry("User4", "Password4")
        entry5 = Entry("User5", "Password5")
        entry6 = Entry("User6", "Password6")
        DatabaseFunctions.addEntry(Cursor, entry1)    
        DatabaseFunctions.addEntry(Cursor, entry2)
        DatabaseFunctions.addEntry(Cursor, entry3)
        DatabaseFunctions.addEntry(Cursor, entry4)
        DatabaseFunctions.addEntry(Cursor, entry5)
        DatabaseFunctions.addEntry(Cursor, entry6)


    def testEntryObject(self):
        entry1 = Entry("User1", "Password1")
        entry2 = Entry("User2", "Password2")
        entry3 = Entry("User3", "Password3")
        self.assertEqual(entry1.purpose , "User1")
        self.assertEqual(entry2.purpose , "User2")
        self.assertEqual(entry3.purpose , "User3")    
        self.assertEqual(entry1.password , "Password1")
        self.assertEqual(entry2.password , "Password2")
        self.assertEqual(entry3.password , "Password3")    
        entry1.password = "Password 7"
        entry2.purpose = "User 8"
        entry3.purpose = "User 9"
        entry3.password = "Password 9"
        self.assertEqual(entry1.purpose , "User1")
        self.assertEqual(entry2.purpose , "User 8")
        self.assertEqual(entry3.purpose , "User 9")    
        self.assertEqual(entry1.password , "Password 7")
        self.assertEqual(entry2.password , "Password2")
        self.assertEqual(entry3.password , "Password 9")

    def testPasswordGeneration(self):
        pass

    def testEncryption(self):
        pass
    def cleanup(self):
        os.remove("UVault.db")

    # Connection = sqlite3.connect('UVault.db') 
    # Cursor = Connection.cursor()
    # testDataBase()
    # testPasswordGeneration()
    # testEncryption()
    # os.remove("")
    
if __name__ == '__main__':
    unittest.main()
    


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
