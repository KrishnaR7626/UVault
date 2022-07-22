#!/usr/bin/python3

import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from colorama import Fore, Style, init
import time
def DecryptDataBase():
    # copy contents into memory and decrypt in memeory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return

def CreatePassword(entropy):
    salt = time.time()
    cipher = entropy+str(salt)
    key = hashlib.sha256(cipher.encode())
    return key.hexdigest()
    
def CreateEntry():
    # different Tier Passwords
    purpose = input("What would you like to name this password?\n")
    entropy = input("Please input any random characters for entropy\n")
    password = CreatePassword(entropy)
    print("\nPassword created \n{}: {}".format(purpose,password))
    return purpose, password

def SaveEntry():
    return

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

# CreateEntry()
print(CreateEntry())