import random
import string
character = " " + string.punctuation + string.digits + string.ascii_letters
character = list(character)
key = character.copy()
random.shuffle(key)

normal = input("ENTER MESSAGE TO BE ENCRYPTED : ")
cipher = ""
for letter in normal:
    index = character.index(letter)
    cipher += key[index]

print(f"original message : {normal}")
print(f"encrypted message: {cipher}")
cipher = input("ENTER MESSAGE TO BE DENCRYPTED : ")
normal = ""
for letter in cipher:
    index = key.index(letter)
    normal += character[index]
print(f"encrypted message: {cipher}")
print(f"original message : {normal}")
