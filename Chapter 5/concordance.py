#Python Programs Chapter 5 Project 8
#Write a program that displays a concordance for a file. The program should output the unique words and their frequencies in alphabetical order. 
#Variations are to track sequences of two words and their frequencies, or n words and their frequencies.

unique_word_frequency = open(input("Enter the name of your file: "), "r")
user_file_enter = {}
unique_word_measurement = 0

for each_word in unique_word_frequency:
    each_word = each_word.strip()
    each_word = each_word.split()
    unique_word_measurement += 1
    for word in each_word:
        word = word.strip()

        if not word in user_file_enter:
            user_file_enter[word] = []
        user_file_enter[word].append(unique_word_measurement)

for total in sorted(user_file_enter):
    print(total, len(user_file_enter[total]))