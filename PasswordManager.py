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




# file_out = open("encryptedfile.bin", "wb")
# [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
# file_out.close()

# file_in = open("encryptedfile.bin", "rb")
# nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
# cipher = AES.new(key, AES.MODE_GCM, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)
# print(data.decode('UTF-8')) 