from random import randint
import string
import os

#Copy the text to clipboard
def add_text_to_clipboard(text):
    command = 'echo ' + text.strip() + ' | clip'
    os.system(command)
    print("Copied to clipboard!")

#We need a list with all characters so we can select a random character from it
allCharacters = list(string.ascii_letters + string.digits + string.punctuation)

password = ""

#User determines length of the password
characterNumber = int(input("Welcome to password generator. Enter how many characters do you want in your password: "))

#Generating password
for x in range(characterNumber):
    password += allCharacters[randint(0,len(allCharacters)-1)]
print(f"Generated password: {password}")
copyPassToClipboard = input("Do you want to copy this password to clipboard? Y/N: ")
if copyPassToClipboard.lower() == "y" : add_text_to_clipboard(password)
    
    
