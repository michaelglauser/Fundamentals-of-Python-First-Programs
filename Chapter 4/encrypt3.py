#Python Programs Chapter 4 Project 6
#Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5 to code a new encryption algorithm. The algorithm should add 1 to each character’s numeric ASCII value, convert it to a bit string, and shift the bits of this string one place to the left. A single-space character in the encrypted string separates the resulting bit strings.

import binascii

def binary_string(num):
    bit_string = "{0:b}".format(num);
    return bit_string

value_input = input("Enter a string: ")

letters = []

for ltr in value_input:
    ASCII_value = ord(ltr)
    next_letter = int(ASCII_value) + 1
    binary_conversion = binary_string(next_letter)
    encryption_variable = binary_conversion[1:]+binary_conversion[0]
    letters.append(encryption_variable)

output = ""

for letter_encrypt in letters:
    output += letter_encrypt + " "

print(output)