from random import randint
import string
import os


def add_text_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


allCharacters = list(string.ascii_letters + string.digits + string.punctuation)
password = ""
characterNumber = int(input("Welcome to password generator. How many characters do you want in your password? "))
for x in range(characterNumber):
    password += allCharacters[randint(0,len(allCharacters)-1)]
print(f"Generated password: {password}")
userInput = input("Do you want to copy this password to clipboard? Y/N: ")
if userInput.lower() == "y":
    add_text_to_clipboard(password)
    print("Copied to clipboard!")
