#Python Programs Chapter 6 Project 7
#Write a recursive function that expects a pathname as an argument. The pathname can be either the name of a file or the name of a directory. 
#If the pathname refers to a file, its name is displayed, followed by its contents. 
#Otherwise, if the pathname refers to a directory, the function is applied to each name in the directory. 

import os

def define_file_or_directory(pathname):

    if os.path.isfile(pathname):
        print("File name:", pathname)

        if not pathname.endswith(".txt"):
            return

        file = open(pathname)

        for line in file:
            if not line.endswith("\n"):
                line += "\n"
            print(line, end="")

        file.close()

    elif os.path.isdir(pathname):

        print("Directory name:", pathname)

        if not pathname.endswith("//"):
            pathname += "/"
            
        for file in os.listdir(pathname):
            define_file_or_directory(pathname + file)


if __name__ == "__main__":
    define_file_or_directory(os.getcwd())
