#Python Programs Chapter 4 Project 1
#Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher. The script should work for any printable characters.

plaintext_message = input("Enter your plaintext message: ")
distance = int(input("Enter the distance value: "))
code = ""
for character in plaintext_message:
    arrangement_value = ord(character)
    Caesar_cipher = arrangement_value + distance
    if Caesar_cipher > ord('z'):
        Caesar_cipher = ord('a') + distance - (ord('z') - arrangement_value + 1)
    code = code + chr(Caesar_cipher)
print(code)