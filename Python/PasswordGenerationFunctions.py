import random
import hashlib
import os
import time

def generateKey(entropy, salt):
    if salt == None:
        salt = time.time()
    cipher = entropy+str(salt)  
    key = hashlib.sha256(cipher.encode())
    return key.hexdigest()

def generatePin(length):
    pin = ""
    for i in range(length):
        pin+=str(random.randint(0,9))
    return pin
    
def generatePassword(path):
    if path == None:
        path = "WordList.txt"
    file = open(path, 'r')

    words = file.readlines()
    password = ""
    for i in range(3):
        password+=words[random.randint(0, len(words)-1)][:-1]
        password+=str(random.randint(0,1000))
    file.close()
    return password