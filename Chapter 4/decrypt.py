#Python Programs Chapter 4 Project 2
# Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a Caesar cipher. The script should work for any printable characters.

coded_message = input("Enter your coded message: ")
distance = int(input("Enter the distance value: "))
plaintext_message = ''
for character in coded_message:
    arrangement_value = ord(character)
    Caesar_cipher = arrangement_value - distance
    plaintext_message += chr(Caesar_cipher)
print(plaintext_message)