#Python Programs Chapter 3 Project 2
#Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle.

import math

a=int(input("Enter the length of the first side of the triangle: "))
b=int(input("Enter the length of the second side of the triangle: "))
c=int(input("Enter the length of the third side of the triangle: "))

a_length = int(a * a)
b_length = int(b * b)
c_length = int(c * c)

total_length = int(a_length + b_length + c_length)
list = [a_length, b_length, c_length]
hypotenuse = max(list)

if int(total_length - hypotenuse) == int(hypotenuse):
    print("The triangle is a right triangle")
else:
    print ("The triangle is not a right triangle")


