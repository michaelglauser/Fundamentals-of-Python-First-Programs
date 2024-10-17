#Python Programs Chapter 3 Project 8
#Write a program that lets the user enter two integers and then prints each step in the process of using the Euclidean algorithm to find their GCD.

import math

smaller_number = int(input("Enter the smaller number: "))
larger_number = int(input("Enter the larger number: "))

greatest_common_divisor = math.gcd(smaller_number,larger_number)

print("\nThe greatest common divisor for these numbers is "+ str(greatest_common_divisor))