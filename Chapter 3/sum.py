#Python Programs Chapter 3 Project 9
# Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average.

import math

series_of_numbers = int(input("Enter a series of numbers: "))
sum = 0
for i in range(series_of_numbers):
    sum += int(input(f"{i+1}.Enter a number: "))

print(sum/series_of_numbers)



#("\nThe sum of your numbers, and their averages is " + )