#!/usr/bin/python3
import PasswordGenerationFunctions as Dbfs
import hashlib
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
import os




# os.chdir("../Database")
# exception = [1, 1, 1]
# salt = get_random_bytes(256)
# with open("salt", "wb") as saltfile:
#     saltfile.write(salt)
#     exception[0] = 0

# with open("UVault.db", "rb") as datafile:
#     data = datafile.read()
#     exception[1] = 0

# with open("UVault.enc", "wb") as dataenc:
#     key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
#     cipher = AES.new(key, AES.MODE_GCM)
#     ciphertext, tag = cipher.encrypt_and_digest(data)
#     [dataenc.write(x) for x in (cipher.nonce, tag, ciphertext) ]
#     exception[2] = 0
# if 1 in exception:
#     os.chdir("../Python")
# else:
#     os.remove("UVault.db")
# os.chdir("../Python")
# print("Done Encrypting and saving")


os.chdir("../Database")
exception = [1, 1, 1]
with open("salt", "rb") as saltfile:
    salt = saltfile.read()
    exception[0] = 0

with open("UVault.enc", "rb") as dataenc:
    nonce, tag, ciphertext = [ dataenc.read(x) for x in (16, 16, -1) ]
    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    exception[1] = 0

with open("UVault.db", "wb") as datafile:
    datafile.write(data)
    exception[2] = 0

if 1 in exception :#or checksum(Cursor):
    os.chdir("../Python")
else:
    os.remove("UVault.enc")