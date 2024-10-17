#Python Programs Chapter 4 Project 4
#Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal and decimal representations of integers.


octal_digit_string = input("Enter a string of octal digits: ")
decimal_value = 0
exponent_value = len(octal_digit_string) - 1
for digit in octal_digit_string:
    decimal_value = decimal_value + int(digit) * 8 ** exponent_value
    exponent_value = exponent_value - 1
print("The integer value is", decimal_value)