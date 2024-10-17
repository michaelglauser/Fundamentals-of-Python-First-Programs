#Python Programs Chapter 5 Project 3
#Write a program that allows the user to navigate the lines of text in a file.
#The program should prompt the user for a filename and input the lines of text into a list.
#The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
#Actual line numbers range from 1 to the number of lines in the file.
#If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.

import random


def getWords(file_name):
    input_file = open(file_name, 'r')
    words = []
    for line in input_file:
        words.extend(line.split())
    return tuple(words)


nouns = getWords("Documents/pythonprojects/nouns.txt")
verbs = getWords("Documents/pythonprojects/verbs.txt")
articles = getWords("Documents/pythonprojects/articles.txt")
prepositions = getWords("Documents/pythonprojects/prepositions.txt")


def noun_text():
    return random.choice(articles) + " " + random.choice(nouns)

def prepositional_text():
    return random.choice(prepositions) + " " + noun_text()

def verb_text():
    return random.choice(verbs) + " " + noun_text() + " " + prepositional_text()

def sentence():
    return noun_text() + " " + verb_text()

def main():
    number = int(input("Enter the lines of text: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
