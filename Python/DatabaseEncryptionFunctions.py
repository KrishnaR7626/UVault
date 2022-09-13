# File encryption functions
import DatabaseFunctions
import cryptography
from DatabaseFunctions import retrieveEntry

def encryptDatabase(password):
    data=b"DATA_TO_BE_ENCRYPTED"
    password=b"PASSWORD"
    salt = get_random_bytes(32)

    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    filewrite = open("UVault.enc", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()

def decryptDatabase(key):
    file_in = open("encryptedfile.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print(data.decode('UTF-8')) 
    # copy contents into memory and decrypt in memory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return checksum()



def checksum(Cursor):
    value = retrieveEntry(Cursor, "checksum")
    if value == "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5":
        return True
    else:
        return False