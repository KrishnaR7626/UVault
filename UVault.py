#!/usr/bin/python3

import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
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
    Connection = sqlite3.connect('UVault.sql') 
    Cursor = Connection.cursor()
    Cursor.execute("CREATE TABLE Passwords (purpose TEXT, password TEXT)")

def encryptDatabase(key):
    return

def decryptDatabase(key):
    # copy contents into memory and decrypt in memory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return

def checksum():
    return

def addEntry(purpose, password):
    try:
        Cursor = sqlite3.connect('UVault.sql').cursor()
        Cursor.execute("INSERT INTO Passwords Values ({}, {})".format(purpose, password))
    except:
        print("Error adding entry to database")    

def removeEntry():
    return

def changeEntry():
    return

def getEntry():
    return

#========================================================================================================
# Main helper functions
def CheckAnswer(answer):
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False

def CheckState():
    directories = os.listdir()
    if "UVault.sql" in directories:
        return True
    else:
        print("Password database not found")
        return False

def CreateNewPassword():
    purpose = input("What would you like to name this password?\n")
    entropy = input("Please input any random characters for entropy\n")
    password = CreatePasswordKey(entropy)
    print("\nPassword created \n{}: {}".format(purpose,password))
    return purpose, password

#========================================================================================================
# Password Generation Functions
def CreatePasswordKey(entropy):
    salt = time.time()
    cipher = entropy+str(salt)
    key = hashlib.sha256(cipher.encode())
    return key.hexdigest()

def GeneratePin(length):
    pin = ""
    for i in range(length):
        pin+=random.randint(1,10)
    return pin
    
def generatePassword():
    return


#========================================================================================================

#========================================================================================================
# User Interface Functions
def display(text, numNL):
    print(text)
    print("\n"*numNL)

def Banner():
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "")
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

# Banner()
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
