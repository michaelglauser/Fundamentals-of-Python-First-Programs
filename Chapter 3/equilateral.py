#Python Programs Chapter 3 Project 1
#Write a program that accepts the lengths of three sides of a triangle. The program output should indicate whether or not the triangle is an equilateral triangle.

import math

a=int(input("Enter the length of the first side of the triangle: "))
b=int(input("Enter the length of the second side of the triangle: "))
c=int(input("Enter the length of the third side of the triangle: "))

if a==b==c:
    print("The triangle is an equilateral triangle.")
else:
    print("The triangle is not an equilateral triangle.")