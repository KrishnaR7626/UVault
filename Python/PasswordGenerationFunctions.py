import random
import hashlib
import os
import time

def generateKey():
    entropy = input("Please input any random characters for entropy\n")
    salt = time.time()
    cipher = entropy+str(salt)  
    key = hashlib.sha256(cipher.encode())
    return key.hexdigest()

def generatePin():
    length = input("How long would you like the pin to be\n")
    pin = ""
    for i in range(length):
        pin+=str(random.randint(0,9))
    return pin
    
def generatePassword():
    path = "/Resources/WordList.txt"
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