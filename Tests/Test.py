import unittest
import sqlite3
import os
import sys
import time
import random
import hashlib

# Importing procedure
path = os.getcwd()+'/Python'

sys.path.insert(1, path)
from Entry import Entry
import DatabaseFunctions as DatabaseFunctions
import PasswordGenerationFunctions as PasswordGenerationFunctions
import DatabaseEncryptionFunctions as DatabaseEncryptionFunctions

# Removes previous Entry so that it can create a fresh database
os.chdir("Tests")
try:
    os.remove('UVault.db')
    os.remove('salt')
    os.remove('UVault.enc')
except:
    pass
Connection = sqlite3.connect('UVault.db') 
Cursor = Connection.cursor()

def hashfile(file):
   sha256 = hashlib.sha256()
   with open(file,'rb') as content:
       block = 0
       while block != b'':
           block = content.read(1024)
           sha256.update(block)
   return sha256.hexdigest()

class UVaultTests(unittest.TestCase):
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
        DatabaseFunctions.removeEntry(Cursor, "User3")
        DatabaseFunctions.removeEntry(Cursor, "User4")
        DatabaseFunctions.removeEntry(Cursor, "User5")
        DatabaseFunctions.removeEntry(Cursor, "User6")
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User1"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User2"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User3"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User4"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User5"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "User6"), None)
        self.assertEqual(DatabaseFunctions.retrieveEntry(Cursor, "checksum"), "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")



    
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

        for length in range(100):
            self.assertEqual(len(PasswordGenerationFunctions.generatePin(length)) , length)
        os.chdir("..")
        path = os.getcwd()+'/Python/WordList.txt'
        os.chdir("Tests")
        for i in range(100):
            password = PasswordGenerationFunctions.generatePassword(path)
            num = 0
            chars = 0
            for char in password:
                if char.isdigit():
                    num+=1
                chars+=1
            if not chars>=20 and num >= 8:
                #if generated password is not strong enough it fails
                self.fail()
            
    def testEncryptionFunctions(self):
        # Checksum Function Testing
        self.assertTrue(DatabaseEncryptionFunctions.checksum(Cursor))
        DatabaseFunctions.removeEntry(Cursor, "checksum")
        self.assertFalse(DatabaseEncryptionFunctions.checksum(Cursor))
        DatabaseFunctions.addEntry(Cursor, Entry("checksum", "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5"))
        self.assertTrue(DatabaseEncryptionFunctions.checksum(Cursor))
        
        originalHash = hashfile("UVault.db")
        DatabaseEncryptionFunctions.encryptDatabase(str.encode("Password"))
        encryptedHash = hashfile("UVault.enc")
        self.assertNotEqual(originalHash, encryptedHash)
        files = os.listdir()
        if "UVault.db" in files:
            self.fail()

        DatabaseEncryptionFunctions.decryptDatabase(str.encode("Password"))
        self.assertTrue(originalHash,hashfile("UVault.db"))
        self.assertTrue(DatabaseEncryptionFunctions.checksum(Cursor))
        files = os.listdir()
        if "UVault.enc" in files:
            self.fail()


if __name__ == '__main__':
    unittest.main()
    Connection.close()

    