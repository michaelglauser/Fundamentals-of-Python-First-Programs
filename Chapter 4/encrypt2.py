#Python Programs Chapter 4 Project 3
#Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.


input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
distance = int(input("Enter the value of the distance: "))

file_input = open(input_file_name, 'r')
file_output = open(output_file_name, 'w')

code = ""

for line in file_input:
    for ch in line:
        order_value = ord(ch)
        Caesar_cipher = order_value + distance
        if Caesar_cipher > ord('z'):
            Caesar_cipher = ord('a') + distance - \
                        (ord('z') - order_value + 1)
        code += chr(Caesar_cipher)

file_output.write(code)

file_input.close()
file_output.close()