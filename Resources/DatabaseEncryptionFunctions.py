# File encryption functions
import DatabaseFunctions as dbfs

def encryptDatabase(key):
    return

def decryptDatabase(key):
    # copy contents into memory and decrypt in memory leave orignal db as is
    # if changed create new data base encrypt it and delete the old one
    return

def checksum():
    value = dbfs.retrieveEntry("checksum")
    if value == "bccd30e889cb6af72091f5faf246c4f2b2e27fde2fcff73cf86440ce94810af5":
        return True
    else:
        return False