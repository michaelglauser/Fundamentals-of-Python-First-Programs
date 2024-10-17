#Python Programs Chapter 2 Project 5
#Write a program that accepts an object's mass (in kilograms) and velocity (in meters per second) as inputs, and then outputs its momentum.


mass = input("Enter the mass of the object, in kilograms: ")
velocity = input("Enter the velocity of the object, in meters per second: ")

momentum = float(mass) * float(velocity)

print("The total momentum of the object is: " + str(momentum))
