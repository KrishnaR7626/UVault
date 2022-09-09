from PasswordGenerationFunctions import generatePassword
from PasswordGenerationFunctions import generateKey
from PasswordGenerationFunctions import generatePin
from UI import display
import Entry
import os

# Main helper functions
def checkAnswer(answer):
    if answer == 'Y' or answer == 'y':
        return True
    else:
        return False

def checkState():
    os.chdir("../Database")
    files = os.listdir()
    if "UVault.db" in files:
        return True
    else:
        print("Password database not found")
        return False

def createNewPassword():
    answer = True
    answers = [1,2,3,4]
    while answer:
        answer = False
        print("Press 1 to generate a Key")
        print("Press 2 to generate a Pin")
        print("Press 3 to generate a Strong Password")
        print("Press 4 to enter a Custom Password to be stored")
        choice = input()
        if choice not in answers:
            answer = True
            print("Invalid Choice")

    if choice == 1:
        password = generateKey()
    elif choice == 2:
        password = generatePin()
    elif choice == 3:
        password = generatePassword()
    elif choice == 4:
        password = input("Please enter your password now: ")
    
    purpose = input("What would you like to name this password?\n")
    display("\nPassword entry created \n{}: {}".format(purpose,password))

    return purpose, password