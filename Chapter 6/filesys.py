#Python Programs Chapter 6 Project 6
#Add a command to this chapter’s case study program that allows the user to view the contents of a file in the current working directory.
#When the command is selected, the program should display a list of filenames and a prompt for the name of the file to be viewed.

import os, os.path

QUIT = '8'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')

MENU = """1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a file name
7   View the contents of a file
8   Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == '8':
            print("Have a nice day!")
            break

def acceptCommand():
    while True:
        command = input("Enter a number: ")
        if not command in COMMANDS:
            print("Error: Unsupported command.")
        else:
            return command

def runCommand(command):
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is: ", \
              countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is: ", \
              countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter your search string: ")
        list_argument = find_file(target, os.getcwd())
        if not list_argument:
            print("String not found.")
        else:
            for f in list_argument:
                print(f)
    elif command == '7':
        print(os.listdir())
        target = input("Enter a file name from the following names: ")
        viewFile(target)

def viewFile(target):
        list_argument = find_file(target, os.getcwd())
        if not list_argument:
            print("File not found.")
            runCommand('7')
        else:
            with open(target) as f:
                lines = f.readlines()
                print(lines)

def listCurrentDir(dirName):
    """Prints a list of the cwd's contents."""
    sorted_list_argument = os.listdir(dirName)
    for element in sorted_list_argument: print(element)

def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: Name not found.")

def countFiles(path):
    count = 0
    sorted_list_argument = os.listdir(path)
    for element in sorted_list_argument:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count

def countBytes(path):
    count = 0
    sorted_list_argument = os.listdir(path)
    for element in sorted_list_argument:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count

def find_file(target, path):
    files = []
    sorted_list_argument = os.listdir(path)
    for element in sorted_list_argument:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(find_file(target, os.getcwd()))
            os.chdir("..")
    return files

if __name__ == "__main__":
    main()