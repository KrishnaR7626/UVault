#!/usr/bin/python3

import hashlib
from operator import truediv
from Resources.Entry import Entry
# from Cryptodome.Cipher import AES
# from Cryptodome.Random import get_random_bytes
from colorama import Fore, Style, init
import time
import os
import sqlite3
import sys
import getpass
import random
 
#========================================================================================================
# Database Functions
def createDatabase():
    Cursor.execute("CREATE TABLE Passwords(purpose text, password text)")
    entry = Entry("checksum", "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5")
    addEntry(entry)

def addEntry(entry):
    Cursor.execute("INSERT INTO Passwords VALUES(?, ?)", (entry.purpose, entry.password))

def removeEntry(entry):
    Cursor.execute("DELETE FROM Passwords WHERE purpose = ?", (entry.purpose,))
    
def changeEntry(entry):
    Cursor.execute("UPDATE Passwords SET password = ? WHERE purpose = ?",(entry.password, entry.purpose))

def retrieveEntry(purpose):
    Cursor.execute("SELECT password FROM Passwords WHERE purpose = ?", (purpose,))
    password = Cursor.fetchone()
    return password
#========================================================================================================
# File encryption functions

def encryptDatabase(key):
    return

def decryptDatabase(key):
    # copy contents into memory and decrypt in memory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return

def checksum():
    value = retrieveEntry("checksum")
    if value == "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5":
        return True
    else:
        return False

#========================================================================================================
# Main helper functions
def checkAnswer(answer):
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False

def checkState():
    files = os.listdir()
    if "UVault.db" in files:
        return True
    else:
        print("Password database not found")
        return False

def createNewPassword():
    purpose = input("What would you like to name this password?\n")
    entropy = input("Please input any random characters for entropy\n")
    password = CreatePasswordKey(entropy)
    print("\nPassword created \n{}: {}".format(purpose,password))
    return purpose, password


#========================================================================================================
# Password Generation Functions
def createPasswordKey(entropy):
    salt = time.time()
    cipher = entropy+str(salt)
    key = hashlib.sha256(cipher.encode())
    return key.hexdigest()

def generatePin(length):
    pin = ""
    for i in range(length):
        pin+=str(random.randint(0,9))
    return pin
    
def generatePassword():
    path = os.getcwd()+"/Resources/WordList.txt"
    try:
        file = open(path, 'r')
    except:
        print("Error accessing resources, run script within intended directory or check Resources folder for missing files")
    words = file.readlines()
    password = ""
    for i in range(3):
        password+=words[random.randint(0, len(words)-1)][:-1]
        password+=str(random.randint(0,1000))
    return password

#========================================================================================================
# User Interface Functions
def display(text, numNL):
    print(text)
    print("\n"*numNL)

def banner():
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + + "")
    print('-'*65)
    print(r'                                                                   ')
    print(r'88        88  8b           d8                         88           ')
    print(r'88        88  \8b         d8/                         88    ,d     ')
    print(r'88        88   \8b       d8/                          88    88     ')
    print(r'88        88    \8b     d8/  ,adPPYYba,  88       88  88  MM88MMM  ')
    print(r'88        88     \8b   d8/   ""     \Y8  88       88  88    88     ')
    print(r'88        88      \8b d8/    ,adPPPPP88  88       88  88    88     ')
    print(r'Y8a.    .a8P       \888/     88,    ,88  "8a,   ,a88  88    88,    ')
    print(r' \"Y8888Y"/         \8/      \"8bbdP"Y8   \"YbbdP/Y8  88    "Y888  ')
    print('                                                                    ')                                                           
    print("                             Version 0                              ")
    print("                       A project by TheTypingFox                    ")
    print('-'*65 + Style.RESET_ALL)
    print("\n\n\n")

#========================================================================================================
#EntryPoint

banner()
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
def printall():
    Cursor.execute("SELECT purpose FROM Passwords")
    print(Cursor.fetchall())
Connection = sqlite3.connect('UVault.db') 
Cursor = Connection.cursor()
createDatabase()
printall()
# entry = Entry("abc", 123)
# addEntry(entry)
addEntry(Entry("1234","12345123"))
addEntry(Entry("abd","afe"))
addEntry(Entry("234234","sferg"))
printall()
# entry.password = "1235565"
# changeEntry(entry)
# printall()
# removeEntry(entry)
# printall()

Connection.commit()
Connection.close()
