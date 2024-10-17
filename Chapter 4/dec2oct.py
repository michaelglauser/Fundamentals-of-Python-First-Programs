#Python Programs Chapter 4 Project 4
#Write the scripts octalTodecimal_integer_value.py and decimal_integer_valueToOctal.py, which convert numbers between the octal and decimal_integer_value representations of integers.


decimal_integer_value = int(input("Enter a decimal integer value: "))
if decimal_integer_value == 0: 
    print(0)
else:
    print("The octal is:")
    bstring = ""
    while decimal_integer_value > 0:
        remainder = decimal_integer_value % 8
        decimal_integer_value = decimal_integer_value // 8
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal_integer_value, remainder, bstring))
    print("The binary representation of the integer is", bstring)  

