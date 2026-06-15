# Project 3: Random Password Generator
# DecodeLabs Internship | Intern: Aqsa Ismail | Batch 2026
 
import random
import string
 
# all characters combined
all_characters = string.ascii_letters + string.digits + string.punctuation
 
# ask user for length
length = int(input("Enter password length: "))
 
# make password
password = ""
for i in range(length):
    password = password + random.choice(all_characters)
 
# print password
print("Your password:", password)