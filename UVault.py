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
 

def CreateDataBase():
    Connection = sqlite3.connect('UVault.sql') 
    Cursor = Connection.cursor()
    Cursor.execute(
        '''
        CREATE TABLE Passwords
        ([password_name] TEXT, [password] TEXT)
        ''')

def generatePassword():
    return

def DecryptDataBase(key):
    # copy contents into memory and decrypt in memeory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return

def CheckState():
    directories = os.listdir()
    if "UVault.sql" in directories:
        print("Password database found")
        return True
    else:
        print("Password database not found")
        return False

def CheckAnswer(answer):
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False

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
    
def CreateEntry():
    purpose = input("What would you like to name this password?\n")
    entropy = input("Please input any random characters for entropy\n")
    password = CreatePasswordKey(entropy)
    print("\nPassword created \n{}: {}".format(purpose,password))
    return purpose, password

def SaveEntry():
    return

def brk(numberOfNewLines):
    print("\n"*numberOfNewLines)
def display(text, brk):
    print(text)
    brk(brk)

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

Banner()
# CreateEntry()
# CreateDataBase()

if CheckState():
    display("Please enter key to decrypt the password database: ", 0)
    DecryptKey = getpass.getpass()
    DecryptDataBase(DecryptKey)

    display("Select the number of the operation you would like to perform:", 0)
    display("1 \tRetrieve a password?",0)
    display("2 \tCreate a password?",0)
    display("3 \tRemove a password?",0)
    display("4 \tChange a password?",1)
    choice = input()
    display(choice,1)
else:
    newDB = input("would you like to create a new Password Database? (Y/N) ")
    if(CheckAnswer(newDB)):
        CreateDataBase()
    else:
        print("Goodbye!")
        sys.exit()
