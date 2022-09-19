#!/usr/bin/python3
import sqlite3
import os
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


os.chdir("Python")
unlocked = False
Password = None
while not unlocked:
    if checkState():
        Password = input("Encrypted database found please enter the password")
        if decryptDatabase(Password):
            Connection = sqlite3.connect('UVault.db') 
            Cursor = Connection.cursor()
            if checksum(cursor):
                display("Incorrect Password")
            else:
                diplay("Database Unlocked")
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
        print("Press 1 to retrieve a password")
        print("Press 2 to create a password")
        print("Press 3 to delete a password")
        print("Press 4 to update a password")
        print("Press 5 to exit")
        try:
            choice = int(input())
        except:
            pass

    if choice == 1:
        purpose = input("Enter the name of the password or press enter to show all")
        if purpose != "":
            password = retrieveEntry(Cursor, purpose)
        else:
            passwords = retrieveAll(Cursor)
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
            password = generateKey()
        elif choice == 2:
            password = generatePin()
        elif choice == 3:
            password = generatePassword()
        elif choice == 4:
            password = input("Please enter your password now: ")
        
        purpose = input("What would you like to name this password?\n")
        entry = Entry(purpose, password)
        addEntry(entry)
        display("\nPassword entry created \n{}: {}".format(purpose,password))
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        using = False
        encryptDatabase(Password)
os.chdir("..")