#Python Programs Chapter 5 Project 7
#Write a program that inputs a text file. The program should print the unique words in the file in alphabetical order.

unique_words = []
with open("input_text_file.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
       unique_text_file = line.split()
       for each_word in unique_text_file:
           each_word = each_word.strip()
           if each_word not in unique_words:
               unique_words.append(each_word)
unique_words = sorted(unique_words)
print(unique_words)