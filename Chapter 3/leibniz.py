#Python Programs Chapter 3 Project 6
#Write a program that allows the user to specify the number of iterations used in this approximation and that displays the resulting value.

import math

number_of_iterations = int(input("Enter the number of iterations: "))

pi = 0

for i in range(number_of_iterations):
    method = (-1) ** i /(2*i+1)
    pi = pi + method

pi = pi * 4

print("Leibniz's approximation of pi is " + str(pi))