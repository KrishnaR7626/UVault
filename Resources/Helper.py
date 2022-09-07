import os
import PasswordGenerationFunctions as pgfs

# Main helper functions
def checkAnswer(answer):
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False

def checkState():
    files = os.listdir()
    if "UVault.db" in files:
        return True
    else:
        print("Password database not found")
        return False

def createNewPassword():
    purpose = input("What would you like to name this password?\n")
    entropy = input("Please input any random characters for entropy\n")
    password = pgfs.CreatePasswordKey(entropy)
    print("\nPassword created \n{}: {}".format(purpose,password))
    return purpose, password