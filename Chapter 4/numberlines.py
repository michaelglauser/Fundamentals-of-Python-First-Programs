#Python Programs Chapter 4 Project 9
#Write a script named numberlines.py. This script creates a program listing from a source program. This script should prompt the user for the names of two files. The input filename could be the name of the script itself, but be careful to use a different output filename! The script copies the lines of text from the input file to the output file, numbering each line as it goes. The line numbers should be right-justified in 4 columns, so that the format of a line in the output file looks like this example:
#1> This is the first line of text.

from os.path import exists


def text_converter(mode):
    file_name = input("Enter the name of your file: ")
    if not exists(file_name):
        print("Error: this file name does not exist!")
        exists_retry = input("Would you like to try again? (y/n)")
        if exists_retry == "y" or exists_retry == "yes":
            text_converter(mode)
        else:
            quit()
    return open(file_name, mode)


def main():
    print('The input filename is:')
    input_file = text_converter('r')
    print('The output filename is')
    output_file = text_converter('a')
    count = 0
    for line in input_file:
        count += 1
        output_file.write(f"{count}> {line}")


if __name__ == "__main__":
    main()