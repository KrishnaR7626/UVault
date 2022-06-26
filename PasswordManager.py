#!/usr/bin/python3

from cryptography.fernet import Fernet
import hashlib
from getpass import getpass
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def retrieve():
    password = "password"
    # password = getpass()
    key = hashlib.sha512(password.encode())
    print(key.hexdigest())
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext = cipher.encrypt_and_digest(key.hexdigest())
    print(ciphertext)
# def newEntry():
    

retrieve()



