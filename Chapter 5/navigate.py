#Python Programs Chapter 5 Project 2
#Write a program that allows the user to navigate the lines of text in a file.
#The program should prompt the user for a filename and input the lines of text into a list.
#The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
#Actual line numbers range from 1 to the number of lines in the file.
#If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.


input_filename = input("Enter the name of your file: ")
f = open(input_filename, 'r')

lines = []
count = ""

while True:

    line = f.readline()
    if line == "":
        break

    if count == "":
        count = 1
    else:
        count += 1

    lines.append(line)

print("The file has ", count, " lines.")

def main():
    while True:
        request = input("Enter a line number. If you enter 0, the program quits: ")
        if request == "0":
            break
        else:
            item = int(request)-1
            if item >= count:
                print("Line number must be less than ", count)
                print("Your file has ", count, " lines.")
            else:
                print(request," : ", lines[item])

if __name__ == "__main__":
    main()