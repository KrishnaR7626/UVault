#!/usr/bin/python3
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
from Entry import Entry
from UI import display
from UI import banner

import sqlite3
import os
from getpass import getpass

os.chdir("Python")
unlocked = False
Password = None
banner()
while not unlocked:
    try:
        if checkState():
            print("Encrypted database found please enter the password:")
            Password = getpass()
            try:
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
            except:
                display("Error Decrypting Database, Possible incorrect password or bad characters")
        else:
            answer = input("Database not found would you like to create a new database? [Y/N] ")
            if checkAnswer(answer):
                Connection = sqlite3.connect('UVault.db') 
                Cursor = Connection.cursor()
                createDatabase(Cursor)
                if checksum(Cursor):
                    unlocked = True
                    while True:
                        print("Enter password to encrypt database: ")
                        Password = getpass()
                        print("Confirm password: ")
                        password = getpass()
                        if Password == password:
                            display("Successfully created new database")
                            break
                        else:
                            display("Passwords do not match")
                else:
                    display("Error creating database")
            else:
                exit(0)
    except:
        display("Error retrieving files make sure you run the program from the intended directory")
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
            display("Bad input/choice, try again")

    if choice == 1:
        # Retrieving a password
        purpose = input("Enter the name of the password or press enter to show all:\n")
        try:
            if purpose != "":
                password = retrieveEntry(Cursor, purpose)
                print("{}: {}".format(purpose,password))
            else:
                passwords = retrieveAll(Cursor)
                for password in passwords:
                    print(password)
        except:
            display("Error fetching password, possible bad characters")
    elif choice == 2:
        # Creating a password
        choice = 0
        while choice not in answers:
            print("Press 1 to generate a Key")
            print("Press 2 to generate a Pin")
            print("Press 3 to generate a Strong Password")
            print("Press 4 to enter a Custom Password to be stored")
            try:
                choice = int(input())
            except:
                display("Enter an appropriate integer value")
        if choice == 1:
            entropy = input("Enter random characters for entropy: ")
            try:
                password = generateKey(entropy, None)
            except:
                display("Bad character inputs")
        elif choice == 2:
            try:
                length = int(input("How long should the PIN be: "))
            except:
                display("Enter an appropriate integer value")
            password = generatePin(length)
        elif choice == 3:
            password = generatePassword(None)
        elif choice == 4:
            password = input("Please enter your password now: ")
        purpose = input("What would you like to name this password?\n")
        entry = Entry(purpose, password)
        addEntry(Cursor, entry)
        Connection.commit()
        print("Password entry created: \n{}: {}".format(purpose,password))
    elif choice == 3:
        purpose = input("Enter the name of the password to update: ")
        choice = 0
        display("Choose one of the following options to replace the password")
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
            try:
                password = generateKey(entropy, None)
            except:
                display("Bad character inputs")
        elif choice == 2:
            try:
                length = int(input("How long should the PIN be: "))
            except:
                display("Enter an appropriate integer value")
            password = generatePin(length)
        elif choice == 3:
            password = generatePassword(None)
        elif choice == 4:
            password = input("Please enter your password now: ")
        changeEntry(Cursor, Entry(purpose, password))
        Connection.commit()
        display("Updated password {} to {}".format(purpose, password))
    elif choice == 4:
        purpose = input("Enter the name of the password to remove: ")
        try:
            removeEntry(Cursor,purpose)
            Connection.commit()
            display("Removed password entry: {}: {}".format(purpose, password))
        except:
            display("Error removing password entry")
    else:
        try:
            Connection.close()
            print("Database connection closed")
            using = False
            encryptDatabase(str.encode(Password))
            print("Exiting")
        except:
            print("Error closing database")
os.chdir("..")
