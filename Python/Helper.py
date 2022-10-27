from PasswordGenerationFunctions import generatePassword
from PasswordGenerationFunctions import generateKey
from PasswordGenerationFunctions import generatePin
from UI import display
import Entry
import os

# Main helper functions
def checkAnswer(answer):
    answer = str(answer)
    if answer == 'Y' or answer == 'y'or answer == None:
        return True
    else:
        return False

def checkState():
    files = os.listdir()
    if "UVault.enc" in files:
        return True
    else:
        return False
