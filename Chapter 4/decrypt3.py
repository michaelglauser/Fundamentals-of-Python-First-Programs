#Python Programs Chapter 4 Project 7
#Write a script that decrypts a message coded by the method used in project 6

import binascii

def binary_string(num):
    bit_string = int(num, 2)
    bit_string = bit_string - 1

    ASCII_value = chr(bit_string)
    return ASCII_value

value_input = input("Enter a string: ")

letters = []

splitText = value_input.split()

for textValues in splitText:
    binary_conversion = textValues[-1:]+textValues[0:-1]
    encryption_variable = binary_string(binary_conversion)
    letters.append(encryption_variable)

output = ""

for bit in letters:
    output += bit
print(output)