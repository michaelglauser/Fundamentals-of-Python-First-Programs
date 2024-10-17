#Python Programs Chapter 3 Project 5
#Write a program that a local biologist can use to predict population growth.


initial_number_of_organisms = int(input("Enter the initial number of organisms: "))
rate_of_growth = float(input("Enter a real number greater than 0 that serves as the rate of growth: "))
number_of_hours_achieve_rate = int(input("Enter the number of hours to achieve the rate of growth: "))
hours_during_population_grows = int(input("Enter the total hours of growth: "))

hours_rate = hours_during_population_grows // number_of_hours_achieve_rate

for number in range(0, hours_rate):
    initial_number_of_organisms = initial_number_of_organisms * rate_of_growth


print("The total predicted population after growth is", initial_number_of_organisms)