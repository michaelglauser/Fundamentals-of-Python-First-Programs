#Python Programs Chapter 4 Project 8
#Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file.


first_file_name = input("Enter the input file name: ")
second_file_name = input("Enter the output file name: ")

first_file = open(first_file_name,'r')
second_file = open(second_file_name, 'w')

for line in first_file:
    second_file.write(line)
first_file.close()
second_file.close()