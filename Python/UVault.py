#!/usr/bin/python3
import sqlite3
import os
from getpass import getpass

from DatabaseEncryptionFunctions import decryptDatabase
from DatabaseEncryptionFunctions import encryptDatabase
from DatabaseEncryptionFunctions import checksum
from PasswordGenerationFunctions import generatePassword
from PasswordGenerationFunctions import generateKey
from PasswordGenerationFunctions import generatePin
from DatabaseFunctions import createDatabase
from DatabaseFunctions import addEntry
from DatabaseFunctions import removeEntry
from DatabaseFunctions import changeEntry
from DatabaseFunctions import retrieveEntry
from DatabaseFunctions import retrieveAll
from Helper import checkState
from Helper import checkAnswer
from UI import display
from UI import banner
from Entry import Entry


os.chdir("Python")
unlocked = False
Password = None
banner()
while not unlocked:
    if checkState():
        print("Encrypted database found please enter the password")
        Password = getpass()
        if decryptDatabase(str.encode(Password)):
            Connection = sqlite3.connect('UVault.db')
            Cursor = Connection.cursor()
            if checksum(Cursor):
                display("Incorrect Password")
            else:
                display("Database Unlocked")
                unlocked = True
        else:
            display("Error Decrypting Database")
    else:
        answer = input("Database not found would you like to create a new database? [Y/N] ")
        if checkAnswer(answer):
            Connection = sqlite3.connect('UVault.db') 
            Cursor = Connection.cursor()
            createDatabase(Cursor)
            if checksum(Cursor):
                unlocked = True
                display("Successfully created new database")
                while True:
                    print("Enter password to encrypt database: ")
                    Password = getpass()
                    print("Confirm password: ")
                    password = getpass()
                    if Password == password:
                        break
                    else:
                        display("Passwords do not match")
            else:
                display("Error creating database")
        else:
            exit(0)
using = True
Connection = sqlite3.connect('UVault.db') 
Cursor = Connection.cursor()
display("Connection to database successful")
while using:
    answers = [1,2,3,4,5]
    choice = 0
    while choice not in answers: 
        print("\nPress 1 to retrieve a password")
        print("Press 2 to create a password")
        print("Press 3 to update a password")
        print("Press 4 to delete a password")
        print("Press 5 to exit")
        try:
            choice = int(input())
        except:
            pass

    if choice == 1:
        purpose = input("Enter the name of the password or press enter to show all:\n")
        if purpose != "":
            password = retrieveEntry(Cursor, purpose)
            print("{}: {}".format(purpose,password))
        else:
            passwords = retrieveAll(Cursor)
            for password in passwords:
                print(password)
    elif choice == 2:
        choice = 0
        while choice not in answers:
            print("Press 1 to generate a Key")
            print("Press 2 to generate a Pin")
            print("Press 3 to generate a Strong Password")
            print("Press 4 to enter a Custom Password to be stored")
            try:
                choice = int(input())
            except:
                pass
        if choice == 1:
            entropy = input("Enter random characters for entropy: ")
            password = generateKey(entropy, None)
        elif choice == 2:
            length = int(input("How long should the PIN be: "))
            password = generatePin(length)
        elif choice == 3:
            password = generatePassword(None)
        elif choice == 4:
            password = input("Please enter your password now: ")
        purpose = input("What would you like to name this password?\n")
        entry = Entry(purpose, password)
        addEntry(Cursor, entry)
        Connection.commit()
        display("Password entry created: \n{}: {}:".format(purpose,password))
    elif choice == 3:
        purpose = input("Enter the name of the password to update: ")
        choice = 0
        while choice not in answers:
            print("Press 1 to generate a Key")
            print("Press 2 to generate a Pin")
            print("Press 3 to generate a Strong Password")
            print("Press 4 to enter a Custom Password to be stored")
            try:
                choice = int(input())
            except:
                pass
        if choice == 1:
            entropy = input("Enter random characters for entropy: ")
            password = generateKey(entropy, None)
        elif choice == 2:
            length = int(input("How long should the PIN be: "))
            password = generatePin(length)
        elif choice == 3:
            password = generatePassword(None)
        elif choice == 4:
            password = input("Please enter your password now: ")
        changeEntry(Cursor, Entry(purpose, password))
        Connection.commit()
    elif choice == 4:
        purpose = input("Enter the name of the password to remove: ")
        removeEntry(Cursor,purpose)
        Connection.commit()
    else:
        Connection.close()
        using = False
        encryptDatabase(str.encode(Password))
        print("Exiting")
os.chdir("..")