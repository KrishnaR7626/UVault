import unittest
import sqlite3
import os
import sys
import time
import random
import hashlib

# Importing procedure
os.chdir("..")
path = os.getcwd()+'/Python'

sys.path.insert(1, path)
from Entry import Entry
import DatabaseFunctions as DatabaseFunctions
import PasswordGenerationFunctions as PasswordGenerationFunctions
import DatabaseEncryptionFunctions as DatabaseEncryptionFunctions
os.chdir("Tests")

# Removes previous Entry so that it can create a fresh database
os.remove('UVault.db')


Connection = sqlite3.connect('UVault.db') 
Cursor = Connection.cursor()
class UVaultTests(unittest.TestCase):
    #Done
    def testDataBase(self):
        DatabaseFunctions.createDatabase(Cursor)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "checksum"), "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")
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
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "checksum"), "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User1"), "Password1")        
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User2"), "Password2")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User3"), "Password3")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User4"), "Password4")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User5"), "Password5")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User6"), "Password6")

        DatabaseFunctions.removeEntry(Cursor, "User1")
        DatabaseFunctions.removeEntry(Cursor, "User2")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User1"), None)        
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User2"), None)

        DatabaseFunctions.changeEntry(Cursor, Entry("User3", "Password 3"))        
        DatabaseFunctions.changeEntry(Cursor, Entry("User4", "Password 4"))
        DatabaseFunctions.changeEntry(Cursor, Entry("User5", "Password 5"))
        DatabaseFunctions.changeEntry(Cursor, Entry("User6", "Password 6"))
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "checksum"), "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User3"), "Password 3")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User4"), "Password 4")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User5"), "Password 5")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User6"), "Password 6")

    #Done
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
        salt = time.time()
        entropies = ["abacus","abadan","abaft","abamp","abase","abash","abasia","abasic","abate","abatic","abatis","abaya","abbacy","abbe","abbess","abbey","abbot","abcs","abdias","abduce"]
        for entropy in entropies:
            self.assertEqual(PasswordGenerationFunctions.generateKey(entropy, salt), hashlib.sha256((entropy+str(salt)).encode()).hexdigest())
        def generatePin(length):
            pin = ""
            for i in range(length):
                pin+=str(random.randint(0,9))
            return pin
        pass

    def testEncryption(self):
        pass
   
if __name__ == '__main__':
    unittest.main()
    


