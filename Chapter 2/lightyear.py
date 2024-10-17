#Python Programs Chapter 2 Project 8
#Write a program that calculates and displays the value of a light-year.


import math
light_travel_distance_per_second = int(365 * 24 * math.pow(60,2))
light_travel_pace = int(3 * math.pow(10,8))
total_value_of_a_lightyear = int(light_travel_distance_per_second * light_travel_pace)


print("The total amount of seconds in year is: " + str(light_travel_distance_per_second))

print("The total number of meters traveled per second is " + str(light_travel_pace))

print("The total value/travel distance of the speed of light, over the course of a year is: " + str(total_value_of_a_lightyear) + " total meters.")