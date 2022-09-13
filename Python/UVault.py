#!/usr/bin/python3
import PasswordGenerationFunctions as Dbfs
import hashlib
from Cryptodome.Random import get_random_bytes
password = "password".encode()
for i in range(10):
    salt = get_random_bytes(32)
    print(str(hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)))
#EntryPoint
