#Python Programs Chapter 4 Project 5
#Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit string as an input.


bit_string = input("Enter a string of bits:")

bit_shift = bit_string[1:]+bit_string[0]

print(bit_shift)