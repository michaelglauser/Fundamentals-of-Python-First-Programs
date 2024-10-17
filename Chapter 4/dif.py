#Python Programs Chapter 4 Project 10
#Write a script named dif.py. This script should prompt the user for the names of two text files and compare the contents of the two files to see if they are the same. If they are, the script should simply output "Yes". If they are not, the script should output "No", followed by the first lines of each file that differ from each other. The input loop should read and compare lines from each file. The loop should break as soon as a pair of different lines is found.

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


def is_compare(file_one_input, file_two_input):
    for line_a in file_one_input:
        if line_a != file_two_input.readline():
            return False
    return True


def main():
    print('The input filename for file one is:')
    file_one_input = text_converter('r')
    print('The input filename for file two is:')
    file_two_input = text_converter('r')
    print(is_compare(file_one_input, file_two_input))


if __name__ == "__main__":
    main()