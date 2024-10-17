#Python Programs Chapter 2 Project 9
#Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
#A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
#There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
#A nautical mile is 1 minute of an arc.

import math

kilometer = float(input("Enter the number of kilometers: "))
convert_kilometer_to_nautical_mile = kilometer * (1/10000) * 90 * 60

print("The corresponding number of nautical miles is: " + str(convert_kilometer_to_nautical_mile))













